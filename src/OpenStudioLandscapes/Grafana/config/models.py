import enum
import pathlib
import textwrap
from string import Template
from typing import Dict, List, Union

from OpenStudioLandscapes.engine.config.models import FeatureBaseModel
from pydantic import (
    Field,
    PositiveInt,
)

from OpenStudioLandscapes.Grafana import (
    ASSET_HEADER,
    LOGGER,
    dist,
)


class AlloyConfigTemplate(Template):
    # https://stackoverflow.com/a/48045197
    # https://stackoverflow.com/a/4840619
    delimiter = "$$"

    @classmethod
    def set_delimiter(cls, delimiter):
        cls.delimiter = delimiter


class GrafanaDockerImage(enum.StrEnum):
    enterprise = "docker.io/grafana/grafana-enterprise"
    oss_legacy = "docker.io/grafana/grafana-oss"
    oss = "docker.io/grafana/grafana"


class GrafanaDockerImageVersion(enum.StrEnum):
    latest = "latest"
    latest_ubuntu = "latest-ubuntu"
    main = "main"
    main_ubuntu = "main-ubuntu"
    version_11_6 = "11.6"
    version_11_6_ubuntu = "11.6-ubuntu"


class GrafanaLogLevel(enum.StrEnum):
    DEBUG = "debug"
    INFO = "info"
    main = "main"
    main_ubuntu = "main-ubuntu"
    version_11_6 = "11.6"
    version_11_6_ubuntu = "11.6-ubuntu"


class GrafanaAlloyConfigs(enum.StrEnum):

    # These are pretty much testing configs.
    # I'm still trying to figure out how Alloy works.

    # Setting up Alloy can be pretty complicated. However,
    # Alloy offers a visualization tool for these configs.
    # With a working config in place, visit:
    # http://<alloy_host>:12345/graph

    # https://github.com/grafana/alloy-scenarios/blob/main/docker-monitoring/config.alloy
    ALLOY_DEMO_CONFIG = textwrap.dedent("""
        // ###############################
        // #### Metrics Configuration ####
        // ###############################
        
        // Host Cadvisor on the Docker socket to expose container metrics.
        prometheus.exporter.cadvisor "example" {
          docker_only = true
        }
        
        discovery.relabel "example" {
          targets = prometheus.exporter.cadvisor.example.targets
        
          rule {
            target_label = "job"
            replacement  = "integrations/docker"
          }
        
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a prometheus.scrape component to collect cadvisor metrics.
        prometheus.scrape "scraper" {
          targets    = discovery.relabel.example.output
          forward_to = [ prometheus.remote_write.demo.receiver ]
        
          scrape_interval = "10s"
        }
        
        // Configure a prometheus.remote_write component to send metrics to a Prometheus server.
        prometheus.remote_write "demo" {
          endpoint {
            url = "http://prometheus:9090/api/v1/write"
          }
        }
        
        // ###############################
        // #### Logging Configuration ####
        // ###############################
        
        // Discover Docker containers and extract metadata.
        discovery.docker "linux" {
          host = "unix:///var/run/docker.sock"
        }
        
        // Define a relabeling rule to create a service name from the container name.
        discovery.relabel "logs_integrations_docker" {
          targets = []
        
          rule {
            source_labels = ["__meta_docker_container_name"]
            regex = "/(.*)"
            target_label = "container_name"
          }
      
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a loki.source.docker component to collect logs from Docker containers.
        loki.source.docker "default" {
          host       = "unix:///var/run/docker.sock"
          targets    = discovery.docker.linux.targets
          relabel_rules = discovery.relabel.logs_integrations_docker.rules
          forward_to = [loki.write.local.receiver]
        }
        
        loki.write "local" {
          endpoint {
            url = "http://loki:3100/loki/api/v1/push"
          }
        }
        """)

    ALLOY_TEST_CONFIG_1 = textwrap.dedent("""
        logging {
          level  = "%s"
          format = "logfmt"
        }
        
        # Components:
        # - https://grafana.com/docs/alloy/latest/reference/components/
        local.file_match "system" {
          path_targets = [
            {
              __address__ = "localhost",
              __path__ = "/var/log/*.log",
              job = "varlogs",
            }
          ]
        }
        
        loki.source.file "system" {
          targets = local.file_match.system.targets
          forward_to = [
            loki.write.default.receiver,
          ]
          legacy_positions_file = "/tmp/positions.yaml"
        }
        
        loki.write "default" = {
          endpoint {
            url = "http://loki:3100/loki/api/v1/push"
          }
          external_labels = {}
        }
        
        """ % GrafanaLogLevel.INFO.value)

    # https://github.com/grafana/alloy-scenarios/blob/main/docker-monitoring/config.alloy
    ALLOY_TEST_CONFIG_2 = textwrap.dedent("""
        // ###############################
        // #### Metrics Configuration ####
        // ###############################
        
        // Host Cadvisor on the Docker socket to expose container metrics.
        prometheus.exporter.cadvisor "example" {
          docker_only = true
        }
        
        discovery.relabel "example" {
          targets = prometheus.exporter.cadvisor.example.targets
        
          rule {
            target_label = "job"
            replacement  = "integrations/docker"
          }
        
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a prometheus.scrape component to collect cadvisor metrics.
        prometheus.scrape "scraper" {
          targets    = discovery.relabel.example.output
          forward_to = [ prometheus.remote_write.demo.receiver ]
        
          scrape_interval = "10s"
        }
        
        // Configure a prometheus.remote_write component to send metrics to a Prometheus server.
        prometheus.remote_write "demo" {
          endpoint {
            url = "http://prometheus:9090/api/v1/write"
          }
        }
        
        discovery.relabel "metrics" {
          targets = prometheus.exporter.unix.metrics.targets
          rule {
            target_label = "instance"
            replacement = hostname
          }
          rule {
            target_label = "job"
            replacement = string.format("%s-metrics", hostname)
          }
        }
        
        prometheus.exporter.unix "metrics" {
          disable_collectors = ["ipvs", "btrfs", "infiniband", "xfs", "zfs"]
          enable_collectors = ["meminfo"]
          filesystem {
            fs_types_exclude = "^(autofs|binfmt_misc|bpf|cgroup2?|configfs|debugfs|devpts|devtmpfs|tmpfs|fusectl|hugetlbfs|iso9660|mqueue|nsfs|overlay|proc|procfs|pstore|rpc_pipefs|securityfs|selinuxfs|squashfs|sysfs|tracefs)$"
            mount_points_exclude = "^/(dev|proc|run/credentials/.+|sys|var/lib/docker/.+)($|/)"
            mount_timeout = "5s"
          }
          netclass {
            ignored_devices = "^(veth.*|cali.*|[a-f0-9]{15})$"
          }
          netdev {
            device_exclude = "^(veth.*|cali.*|[a-f0-9]{15})$"
          }
        }
        
        prometheus.scrape "metrics" {
          scrape_interval = "15s"
          targets = discovery.relabel.metrics.output
          forward_to = [prometheus.remote_write.demo.receiver]
        }
        
        // ###############################
        // #### Logging Configuration ####
        // ###############################
        
        // Discover Docker containers and extract metadata.
        discovery.docker "linux" {
          host = "unix:///var/run/docker.sock"
        }
        
        // Define a relabeling rule to create a service name from the container name.
        discovery.relabel "logs_integrations_docker" {
          targets = []
        
          rule {
            source_labels = ["__meta_docker_container_name"]
            regex = "/(.*)"
            target_label = "container_name"
          }
      
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a loki.source.docker component to collect logs from Docker containers.
        loki.source.docker "default" {
          host       = "unix:///var/run/docker.sock"
          targets    = discovery.docker.linux.targets
          relabel_rules = discovery.relabel.logs_integrations_docker.rules
          forward_to = [loki.write.local.receiver]
        }
        
        local.file_match "system" {
          path_targets = [
            {
              __address__ = "localhost",
              __path__ = "/var/log/*.log",
              job = "varlogs",
            },
          ]
        }
        
        loki.source.file "system" {
          targets = local.file_match.system.targets
          forward_to = [
            loki.write.local.receiver,
          ]
          legacy_positions_file = "/tmp/positions.yaml"
        }
        
        loki.write "local" {
          endpoint {
            url = "http://loki:3100/loki/api/v1/push"
          }
        }
        """)

    # https://github.com/grafana/alloy-scenarios/blob/main/docker-monitoring/config.alloy
    # Dashboards:
    # - https://grafana.com/grafana/dashboards/1860-node-exporter-full/
    #   ID: 1860
    # - https://grafana.com/grafana/dashboards/19908-docker-container-monitoring-with-prometheus-and-cadvisor/
    #   ID: 19908
    ALLOY_TEST_CONFIG_3 = textwrap.dedent("""
        // ###############################
        // #### Metrics Configuration ####
        // ###############################
        
        // Host Cadvisor on the Docker socket to expose container metrics.
        prometheus.exporter.cadvisor "example" {
          docker_only = true
        }
        
        discovery.relabel "example" {
          targets = prometheus.exporter.cadvisor.example.targets
        
          rule {
            target_label = "job"
            replacement  = "integrations/docker"
          }
        
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a prometheus.scrape component to collect cadvisor metrics.
        prometheus.scrape "scraper" {
          targets    = discovery.relabel.example.output
          forward_to = [ prometheus.remote_write.demo.receiver ]
        
          scrape_interval = "10s"
        }
        
        // Configure a prometheus.remote_write component to send metrics to a Prometheus server.
        prometheus.remote_write "demo" {
          endpoint {
            // CHANGE ME
            url = "http://prometheus:9090/api/v1/write"
          }
        }
        
        discovery.relabel "metrics" {
          targets = prometheus.exporter.unix.metrics.targets
          rule {
            target_label = "instance"
            replacement = hostname
          }
          rule {
            target_label = "job"
            replacement = string.format("%s-metrics", hostname)
          }
        }
        
        prometheus.exporter.unix "metrics" {
          disable_collectors = ["ipvs", "btrfs", "infiniband", "xfs", "zfs"]
          enable_collectors = ["meminfo"]
          filesystem {
            fs_types_exclude = "^(autofs|binfmt_misc|bpf|cgroup2?|configfs|debugfs|devpts|devtmpfs|tmpfs|fusectl|hugetlbfs|iso9660|mqueue|nsfs|overlay|proc|procfs|pstore|rpc_pipefs|securityfs|selinuxfs|squashfs|sysfs|tracefs)$"
            mount_points_exclude = "^/(dev|proc|run/credentials/.+|sys|var/lib/docker/.+)($|/)"
            mount_timeout = "5s"
          }
          netclass {
            ignored_devices = "^(veth.*|cali.*|[a-f0-9]{15})$"
          }
          netdev {
            device_exclude = "^(veth.*|cali.*|[a-f0-9]{15})$"
          }
        }
        
        prometheus.scrape "metrics" {
          scrape_interval = "15s"
          targets = discovery.relabel.metrics.output
          forward_to = [prometheus.remote_write.demo.receiver]
        }
        
        // ###############################
        // #### Logging Configuration ####
        // ###############################
        
        // Discover Docker containers and extract metadata.
        discovery.docker "linux" {
          host = "unix:///var/run/docker.sock"
        }
        
        // Define a relabeling rule to create a service name from the container name.
        discovery.relabel "docker" {
          targets = []
        
          rule {
            source_labels = ["__meta_docker_container_name"]
            regex = "/(.*)"
            target_label = "container_name"
          }
      
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a loki.source.docker component to collect logs from Docker containers.
        loki.source.docker "docker" {
          host       = "unix:///var/run/docker.sock"
          targets    = discovery.docker.linux.targets
          relabel_rules = discovery.relabel.docker.rules
          forward_to = [loki.write.local.receiver]
        }
        
        // // /var/logs
        // 
        // local.file_match "system" {
        //   path_targets = [
        //     {
        //       __address__ = "localhost",
        //       __path__ = "/var/log/*.log",
        //       job = "varlogs",
        //     },
        //   ]
        // }
        // 
        // loki.source.file "system" {
        //   targets = local.file_match.system.targets
        //   forward_to = [
        //     loki.write.local.receiver,
        //   ]
        //   legacy_positions_file = "/tmp/positions.yaml"
        // }
        
        // journal
        
        // Collect logs from systemd journal for node_exporter integration
        loki.source.journal "journal" {
          // Only collect logs from the last 24 hours
          max_age       = "24h0m0s"
          // Apply relabeling rules to the logs
          relabel_rules = discovery.relabel.journal.rules
          // Send logs to the local Loki instance
          forward_to    = [loki.write.local.receiver]
          // if alloy is running in container, we 
          // need to add the following path
          path = "/var/log/journal"
          labels = {
            component = string.format("%s-journal", hostname),
          }
        }
        
        // Define which log files to collect for node_exporter
        local.file_match "system" {
          path_targets = [{
            // Target localhost for log collection
            __address__ = "localhost",
            // Collect standard system logs
            __path__ = "/var/log/{syslog,messages,*.log}",
            // Add instance label with hostname
            instance = hostname,
            // Add job label for logs
            job = string.format("%s-logs", hostname),
          }]
        }
        
        // Define relabeling rules for systemd journal logs
        discovery.relabel "journal" {
          targets = []
        
          rule {
            // Extract systemd unit information into a label
            source_labels = ["__journal__systemd_unit"]
            target_label  = "unit"
          }
        
          rule {
            // Extract boot ID information into a label
            source_labels = ["__journal__boot_id"]
            target_label  = "boot_id"
          }
        
          rule {
            // Extract transport information into a label
            source_labels = ["__journal__transport"]
            target_label  = "transport"
          }
        
          rule {
            // Extract log priority into a level label
            source_labels = ["__journal_priority_keyword"]
            target_label  = "level"
          }
        }
        
        // Collect logs from files for node_exporter
        loki.source.file "system" {
          // Use targets defined in local.file_match
          targets    = local.file_match.system.targets
          // Send logs to the local Loki instance
          forward_to = [loki.write.local.receiver]
        }
        
        loki.write "local" {
          endpoint {
            // CHANGE ME
            url = "http://loki:3100/loki/api/v1/push"
          }
        }
        
        // Enable live debugging features (empty config means use defaults)
        // - https://grafana.com/docs/alloy/latest/reference/config-blocks/livedebugging/
        // - https://grafana.com/docs/alloy/latest/troubleshoot/debug/
        livedebugging {
          enabled = false
        }
        """)

    ALLOY_TEST_CONFIG_4 = textwrap.dedent("""
        // ###############################
        // #### Metrics Configuration ####
        // ###############################
        
        // Host Cadvisor on the Docker socket to expose container metrics.
        prometheus.exporter.cadvisor "example" {
          docker_only = true
        }
        
        discovery.relabel "example" {
          targets = prometheus.exporter.cadvisor.example.targets
        
          rule {
            target_label = "job"
            replacement  = "integrations/docker"
          }
        
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a prometheus.scrape component to collect cadvisor metrics.
        prometheus.scrape "scraper" {
          targets    = discovery.relabel.example.output
          forward_to = [ prometheus.remote_write.demo.receiver ]
        
          scrape_interval = "10s"
        }
        
        // Configure a prometheus.remote_write component to send metrics to a Prometheus server.
        // - https://grafana.com/docs/alloy/latest/reference/components/prometheus/prometheus.remote_write/
        prometheus.remote_write "demo" {
          endpoint {
            // Endpoints"
            // - https://prometheus.io/docs/prometheus/latest/querying/api/
            //
            // Verify operational:
            // - $$endpoint_prometheus:$$port_prometheus/api/v1/status/config
            url = "$$endpoint_prometheus:$$port_prometheus/api/v1/write"
            // basic_auth {
            //   username = "admin"
            //   password = "admin"
            // }
          }
        }
        
        discovery.relabel "metrics" {
          targets = prometheus.exporter.unix.metrics.targets
          rule {
            target_label = "instance"
            replacement = hostname
          }
          rule {
            target_label = "job"
            replacement = string.format("%s-metrics", hostname)
          }
        }
        
        prometheus.exporter.unix "metrics" {
          disable_collectors = ["ipvs", "btrfs", "infiniband", "xfs", "zfs"]
          enable_collectors = ["meminfo"]
          filesystem {
            fs_types_exclude = "^(autofs|binfmt_misc|bpf|cgroup2?|configfs|debugfs|devpts|devtmpfs|tmpfs|fusectl|hugetlbfs|iso9660|mqueue|nsfs|overlay|proc|procfs|pstore|rpc_pipefs|securityfs|selinuxfs|squashfs|sysfs|tracefs)$"
            mount_points_exclude = "^/(dev|proc|run/credentials/.+|sys|var/lib/docker/.+)($|/)"
            mount_timeout = "5s"
          }
          netclass {
            ignored_devices = "^(veth.*|cali.*|[a-f0-9]{15})$"
          }
          netdev {
            device_exclude = "^(veth.*|cali.*|[a-f0-9]{15})$"
          }
        }
        
        prometheus.scrape "metrics" {
          scrape_interval = "15s"
          targets = discovery.relabel.metrics.output
          forward_to = [prometheus.remote_write.demo.receiver]
        }
        
        // ###############################
        // #### Logging Configuration ####
        // ###############################
        
        // Discover Docker containers and extract metadata.
        discovery.docker "linux" {
          host = "unix:///var/run/docker.sock"
        }
        
        // Define a relabeling rule to create a service name from the container name.
        discovery.relabel "docker" {
          targets = []
        
          rule {
            source_labels = ["__meta_docker_container_name"]
            regex = "/(.*)"
            target_label = "container_name"
          }
      
          rule {
            target_label = "instance"
            replacement  = hostname
          }
        }
        
        // Configure a loki.source.docker component to collect logs from Docker containers.
        loki.source.docker "docker" {
          host       = "unix:///var/run/docker.sock"
          targets    = discovery.docker.linux.targets
          relabel_rules = discovery.relabel.docker.rules
          forward_to = [loki.write.local.receiver]
        }
        
        // // /var/logs
        // 
        // local.file_match "system" {
        //   path_targets = [
        //     {
        //       __address__ = "localhost",
        //       __path__ = "/var/log/*.log",
        //       job = "varlogs",
        //     },
        //   ]
        // }
        // 
        // loki.source.file "system" {
        //   targets = local.file_match.system.targets
        //   forward_to = [
        //     loki.write.local.receiver,
        //   ]
        //   legacy_positions_file = "/tmp/positions.yaml"
        // }
        
        // journal
        
        // Collect logs from systemd journal for node_exporter integration
        loki.source.journal "journal" {
          // Only collect logs from the last 24 hours
          max_age       = "24h0m0s"
          // Apply relabeling rules to the logs
          relabel_rules = discovery.relabel.journal.rules
          // Send logs to the local Loki instance
          forward_to    = [loki.write.local.receiver]
          // if alloy is running in container, we 
          // need to add the following path
          path = "/var/log/journal"
          labels = {
            component = string.format("%s-journal", hostname),
          }
        }
        
        // Define which log files to collect for node_exporter
        local.file_match "system" {
          path_targets = [{
            // Target localhost for log collection
            __address__ = "localhost",
            // Collect standard system logs
            __path__ = "/var/log/{syslog,messages,*.log}",
            // Add instance label with hostname
            instance = hostname,
            // Add job label for logs
            job = string.format("%s-logs", hostname),
          }]
        }
        
        // Define relabeling rules for systemd journal logs
        discovery.relabel "journal" {
          targets = []
        
          rule {
            // Extract systemd unit information into a label
            source_labels = ["__journal__systemd_unit"]
            target_label  = "unit"
          }
        
          rule {
            // Extract boot ID information into a label
            source_labels = ["__journal__boot_id"]
            target_label  = "boot_id"
          }
        
          rule {
            // Extract transport information into a label
            source_labels = ["__journal__transport"]
            target_label  = "transport"
          }
        
          rule {
            // Extract log priority into a level label
            source_labels = ["__journal_priority_keyword"]
            target_label  = "level"
          }
        }
        
        // Collect logs from files for node_exporter
        loki.source.file "system" {
          // Use targets defined in local.file_match
          targets    = local.file_match.system.targets
          // Send logs to the local Loki instance
          forward_to = [loki.write.local.receiver]
        }
        
        loki.write "local" {
          endpoint {
            // Endpoints"
            // - https://grafana.com/docs/loki/latest/reference/loki-http-api/
            //
            // Verify operational:
            // $$endpoint_loki:$$port_loki/metrics
            url = "$$endpoint_loki:$$port_loki/loki/api/v1/push"
          }
        }
        
        // Enable live debugging features (empty config means use defaults)
        // - https://grafana.com/docs/alloy/latest/reference/config-blocks/livedebugging/
        // - https://grafana.com/docs/alloy/latest/troubleshoot/debug/
        livedebugging {
          enabled = false
        }
        """)


ALLOY_CONFIG_TEMPLATE = AlloyConfigTemplate(GrafanaAlloyConfigs.ALLOY_TEST_CONFIG_4)


# Todo
#  - [ ] Fix
#        loki.2026-01-21_17-22-54__seasoned-jelly-wholesale-mixer                                   | level=warn ts=2026-02-20T07:44:36.66288442Z caller=push.go:309 component=pattern-ingester writer=metric-aggregation msg="failed to send entry, retrying" status=-1 error="failed to push payload: Post \"http:///loki/api/v1/push\": http: no Host in request URL"
#  - [ ] Fix
#        alloy_container.compose_scope-default.2026-01-21_17-22-54__seasoned-jelly-wholesale-mixer  | ts=2026-02-20T07:44:41.381091726Z level=error msg="encountered error getting zfs filesystem: miniboss_pool: exec: \"zfs\": executable file not found in $PATH: \"zfs fs list -Hp -o name,origin,used,available,mountpoint,compression,type,volsize,quota,referenced,written,logicalused,usedbydataset miniboss_pool\" => " component_path=/ component_id=prometheus.exporter.cadvisor.example
#  - [x] Fix
#        alloy_container.compose_scope-default.2026-01-21_17-22-54__seasoned-jelly-wholesale-mixer  | ts=2026-02-20T07:44:41.381762451Z level=error msg="encountered error refreshing zfs watcher: exec: \"zfs\": executable file not found in $PATH: \"zfs fs list -Hp -o name,origin,used,available,mountpoint,compression,type,volsize,quota,referenced,written,logicalused,usedbydataset miniboss_pool\" => " component_path=/ component_id=prometheus.exporter.cadvisor.example
#  - [ ] Fix (ComposeScope_worker)
#        Error: /etc/alloy/config.alloy:34:1: Failed to build component: building component: get segment range: segments are not sequential
#        33 |   // Configure a prometheus.remote_write component to send metrics to a Prometheus server.
#        34 |   prometheus.remote_write "demo" {
#           |  _^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#        35 | |   endpoint {
#        36 | |     // Endpoints"
#        37 | |     // - https://prometheus.io/docs/prometheus/latest/querying/api/
#        38 | |     //
#        39 | |     // Verify operational:
#        40 | |     // - http://10.1.2.15:9090/api/v1/status/config
#        41 | |     url = "http://10.1.2.15:9090/api/v1/write"
#        42 | |   }
#        43 | | }
#           | |_^
#        44 |
#        interrupt received
#        Error: could not perform the initial load successfully
#        2026/02/25 19:35:39 collector server run finished with error: could not perform the initial load successfully


class Config(FeatureBaseModel):

    # Todo
    #  - [ ] Use Postgres instead of mysql
    #        - https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#database

    # Configure Grafana:
    # - [Default Paths](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/#default-paths)
    # - [Configure a Grafana Docker image](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/)
    # - Grafana itself does not store metrics. Hence, data remains on the Alloy servers.

    GF_PATHS_DATA: pathlib.Path = Field(
        default=pathlib.Path("{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/var/lib/grafana"),
    )

    feature_name: str = dist.name

    group_name: str = ASSET_HEADER["group_name"]

    key_prefixes: List[str] = ASSET_HEADER["key_prefix"]

    grafana_dashboards: Dict[str, Dict[str, Union[str, int, None]]] = Field(
        default={
            "Node Exporter Full": {
                "url": "https://grafana.com/api/dashboards/1860/revisions/42/download",
                "id": 1860,
                # "requires_extra_variables": [],
            },
            "cAdvisor Docker Insights": {
                "url": "https://grafana.com/api/dashboards/19908/revisions/1/download",
                "id": 19908,
                # "requires_variables": [
                #     {
                #         "requires_extra_variables": "Data source",
                #         "name": "DS_PROMETHEUS",
                #         "label": "Datasource",
                #         "variable_options": {
                #             "type": "prometheus",
                #         },
                #     },
                # ],
            },
        },
        frozen=False,  # outfile will be set dynamically
    )

    grafana_admin_user: str = Field(
        default="openstudiolandscapes",
        description="https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#admin_user",
        frozen=True,
    )

    grafana_admin_password: str = Field(
        default="openstudiolandscapes",
        description="https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#admin_password",
        frozen=True,
    )

    grafana_root_url: str = Field(
        default="http://localhost:3000",
        description="https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#root_url",
        frozen=True,
    )

    grafana_port_container: PositiveInt = Field(
        default=3000,
        description="The Grafana container port.",
        frozen=True,
    )
    grafana_port_host: PositiveInt = Field(
        default=3030,
        description="The Grafana host port.",
        frozen=False,
    )

    grafana_loki_port_container: PositiveInt = Field(
        default=3100,
        description="The Grafana Loki container port.",
        frozen=True,
    )
    grafana_loki_port_host: PositiveInt = Field(
        default=3100,
        description="The Grafana Loki host port.",
        frozen=False,
    )
    grafana_loki_loglevel: GrafanaLogLevel = Field(
        default=GrafanaLogLevel.INFO,
        description="The Grafana Loki loglevel.",
        examples=[i.name for i in GrafanaLogLevel],
    )

    prometheus_port_container: PositiveInt = Field(
        default=9090,
        description="The Prometheus container port.",
        frozen=True,
    )
    prometheus_port_host: PositiveInt = Field(
        default=9090,
        description="The Prometheus host port.",
        frozen=False,
    )

    # prometheus_data: pathlib.Path = Field(
    #     default=pathlib.Path("{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/prometheus/data"),
    # )

    # grafana_mimir_port_container: PositiveInt = Field(
    #     default=9009,
    #     description="The Grafana Mimir container port.",
    #     frozen=True,
    # )
    # grafana_mimir_port_host: PositiveInt = Field(
    #     default=9009,
    #     description="The Grafana Mimir host port.",
    #     frozen=False,
    # )

    grafana_image: GrafanaDockerImage = Field(
        default=GrafanaDockerImage.oss,
        examples=[i.name for i in GrafanaDockerImage],
    )

    grafana_image_version: GrafanaDockerImageVersion = Field(
        default=GrafanaDockerImageVersion.latest_ubuntu,
        examples=[i.name for i in GrafanaDockerImageVersion],
    )

    grafana_loki_image: str = Field(
        default="docker.io/grafana/loki:latest",
        # examples=[i.name for i in GrafanaDockerImage],
    )

    prometheus_image: str = Field(
        default="docker.io/prom/prometheus:main",  # latest?
        # examples=[i.name for i in GrafanaDockerImage],
    )

    alloy_image: str = Field(
        default="docker.io/grafana/alloy:latest",
    )

    # HttpUrl adds a trailing slash, which is undesirable
    endpoint_prometheus: str = Field(
        default="http://prometheus",
    )

    # HttpUrl adds a trailing slash, which is undesirable
    endpoint_loki: str = Field(
        default="http://loki",
    )

    # grafana_mimir_image: str = Field(
    #     default="docker.io/grafana/mimir:latest",
    #     # examples=[i.name for i in GrafanaDockerImage],
    # )

    alloy_config_template: GrafanaAlloyConfigs = Field(
        default=GrafanaAlloyConfigs.ALLOY_TEST_CONFIG_4,
        # Exclude Field from Model Serialization
        exclude=True,
    )

    alloy_apt_packages: List[str] = Field(
        default=[
            "zfsutils-linux",
        ],
        # description="`boto3` is required if `kitsu_enable_job_queue` is `true`. [Reference](https://zou.cg-wire.com/jobs/)",
        frozen=True,
    )

    # @field_validator('alloy_config_4', mode='before')
    # @classmethod
    # def substitute(cls, value: str) -> str:
    #     template = AlloyConfigTemplate(value)
    #     ret = template.substitute(
    #         endpoint_prometheus=cls.endpoint_prometheus,
    #         port_prometheus=cls.prometheus_port_container,
    #         endpoint_loki=cls.endpoint_loki,
    #         port_loki=cls.grafana_loki_port_container,
    #     )
    #     return ret

    # SUBSTITUTED TEMPLATE
    @property
    def alloy_config(self) -> str:
        template = AlloyConfigTemplate(self.alloy_config_template)
        ret = template.substitute(
            endpoint_prometheus=self.endpoint_prometheus,
            # Todo
            #  - [ ] not sure yet whether _port_container or _port_host
            port_prometheus=self.prometheus_port_container,
            endpoint_loki=self.endpoint_loki,
            # Todo
            #  - [ ] not sure yet whether _port_container or _port_host
            port_loki=self.grafana_loki_port_container,
        )
        return ret

    # EXPANDABLE PATHS
    @property
    def GF_PATHS_DATA_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")
        LOGGER.debug(f"Expanding {self.GF_PATHS_DATA}...")
        ret = pathlib.Path(
            self.GF_PATHS_DATA.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret


if __name__ == "__main__":
    CONFIG_STR: str = Config.get_docs()
else:
    import yaml

    schema: Dict = Config.model_json_schema(mode="serialization")
    properties: Dict = schema.get("properties", {})

    CONFIG_STR: str = yaml.dump(properties)
