import enum
import textwrap
from typing import List

from dagster import get_dagster_logger
from pydantic import (
    Field,
    PositiveInt,
)

LOGGER = get_dagster_logger(__name__)

from OpenStudioLandscapes.engine.config.models import FeatureBaseModel
from OpenStudioLandscapes.engine.config.str_gen import get_config_str

from OpenStudioLandscapes.Grafana import constants, dist


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
    ALLOY_DEMO_CONFIG = textwrap.dedent(
        """
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
            replacement  = constants.hostname
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
            replacement  = constants.hostname
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
        """
    )

    ALLOY_TEST_CONFIG_1 = textwrap.dedent(
        """
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
        
        """ % GrafanaLogLevel.INFO.value
    )

    # https://github.com/grafana/alloy-scenarios/blob/main/docker-monitoring/config.alloy
    ALLOY_TEST_CONFIG_2 = textwrap.dedent(
        """
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
            replacement  = constants.hostname
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
            replacement  = constants.hostname
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
        """
    )


class Config(FeatureBaseModel):

    feature_name: str = dist.name

    group_name: str = constants.ASSET_HEADER["group_name"]

    key_prefixes: List[str] = constants.ASSET_HEADER["key_prefix"]

    grafana_admin_user: str = Field(
        default="openstudiolandscapes",
        description="The Grafana Admin username.",
        frozen=True,
    )

    grafana_admin_password: str = Field(
        default="openstudiolandscapes",
        description="The Grafana Admin password.",
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

    # grafana_mimir_image: str = Field(
    #     default="docker.io/grafana/mimir:latest",
    #     # examples=[i.name for i in GrafanaDockerImage],
    # )

    alloy_config: GrafanaAlloyConfigs = Field(
        default=GrafanaAlloyConfigs.ALLOY_TEST_CONFIG_2,
    )


CONFIG_STR = get_config_str(
    Config=Config,
)
