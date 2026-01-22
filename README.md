[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Grafana](#feature-openstudiolandscapes-grafana)
   1. [Brief](#brief)
   2. [Install](#install)
   3. [Configure](#configure)
      1. [Default Configuration](#default-configuration)
2. [External Resources](#external-resources)
   1. [Official Documentation](#official-documentation)
      1. [Grafana Alloy](#grafana-alloy)
   2. [Configure Grafana](#configure-grafana)
      1. [Default Paths](#default-paths)
      2. [`defaults.ini`](#defaultsini)
      3. [`grafana.ini`](#grafanaini)
3. [Community](#community)

***

This `README.md` was dynamically created with [OpenStudioLandscapesUtil-ReadmeGenerator](https://github.com/michimussato/OpenStudioLandscapesUtil-ReadmeGenerator).

***

# Feature: OpenStudioLandscapes-Grafana

## Brief

This is an extension to the OpenStudioLandscapes ecosystem. The full documentation of OpenStudioLandscapes is available [here](https://github.com/michimussato/OpenStudioLandscapes).

> [!NOTE]
> 
> You feel like writing your own Feature? Go and check out the 
> [OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template).

## Install

Clone this repository into `OpenStudioLandscapes/.features` (assuming the current working directory to be the Git repository root `./OpenStudioLandscapes`):

```shell
git -C ./.features clone https://github.com/michimussato/OpenStudioLandscapes-Grafana.git
# Check out a specific branch with:
# List branches: 
# git -C ./.features/OpenStudioLandscapes-Grafana branch -a
# Checkout branch: 
# git -C ./.features/OpenStudioLandscapes-Grafana checkout <branch>
```

Install into OpenStudioLandscapes `venv` (`./OpenStudioLandscapes/.venv`):

```shell
source .venv/bin/activate
# python -m pip install --upgrade pip setuptools
# the following removes the `openstudiolandscapes` executable for now (will be fixed soon)
pip install -e "./.features/OpenStudioLandscapes-Grafana"
# so, re-install `OpenStudioLandscapes` engine:
pip install -e "."
```

For more info on `pip` see [VCS Support of `pip`](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Configure

OpenStudioLandscapes will search for a local config store. The default location is `~/.config/OpenStudioLandscapes/config-store/` but you can specify a different location if you need to.

A local config store location will be created if it doesn't exist, together with the `config.yml` files for each individual Feature.

> [!TIP]
> 
> The config store root will be initialized as a local Git
> controlled repository. This makes it easy to track changes
> you made to the `config.yml`.

> [!TIP]
> 
> To specify a config store location different than
> the default, you can do so by setting the environment variable
> `OPENSTUDIOLANDSCAPES__CONFIGSTORE_ROOT`:
> 
> ```shell
> OPENSTUDIOLANDSCAPES__CONFIGSTORE_ROOT="~/.config/OpenStudioLandscapes/my-custom-config-store"
> ```

The following settings are available in `OpenStudioLandscapes-Grafana` and are based on [`OpenStudioLandscapes-Grafana/tree/main/OpenStudioLandscapes/Grafana/config/models.py`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/OpenStudioLandscapes/Grafana/config/models.py).

### Default Configuration


<details>
<summary><code>config.yml</code></summary>


```yaml
# ===
# env
# ---
#
# Type: typing.Dict
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# =============
# config_engine
# -------------
#
# Type: <class 'OpenStudioLandscapes.engine.config.models.ConfigEngine'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# =============
# config_parent
# -------------
#
# Type: <class 'OpenStudioLandscapes.engine.config.models.FeatureBaseModel'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# ============
# distribution
# ------------
#
# Type: <class 'importlib.metadata.Distribution'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         None
# Description:
#     None
# Required:
#     False
# Examples:
#     None


# ==========
# group_name
# ----------
#
# Type: <class 'str'>
# Base Class Info:
#     Required:
#         True
#     Description:
#         Dagster Group name. This will represent the group node name. See https://docs.dagster.io/api/dagster/assets for more information
#     Default value:
#         PydanticUndefined
# Description:
#     None
# Required:
#     False
# Examples:
#     None
group_name: OpenStudioLandscapes_Grafana


# ============
# key_prefixes
# ------------
#
# Type: typing.List[str]
# Base Class Info:
#     Required:
#         True
#     Description:
#         Dagster Asset key prefixes. This will be reflected in the nesting (directory structure) of the Asset. See https://docs.dagster.io/api/dagster/assets for more information
#     Default value:
#         PydanticUndefined
# Description:
#     None
# Required:
#     False
# Examples:
#     None
key_prefixes:
- OpenStudioLandscapes_Grafana


# =======
# enabled
# -------
#
# Type: <class 'bool'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         Whether the Feature is enabled or not.
#     Default value:
#         True
# Description:
#     Whether the Feature is enabled or not.
# Required:
#     False
# Examples:
#     None


# =============
# compose_scope
# -------------
#
# Type: <class 'str'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         None
#     Default value:
#         default
# Description:
#     None
# Required:
#     False
# Examples:
#     ['default', 'license_server', 'worker']


# ============
# feature_name
# ------------
#
# Type: <class 'str'>
# Base Class Info:
#     Required:
#         True
#     Description:
#         The name of the feature. It is derived from the `OpenStudioLandscapes.<Feature>.dist` attribute.
#     Default value:
#         PydanticUndefined
# Description:
#     None
# Required:
#     False
# Examples:
#     None
feature_name: OpenStudioLandscapes-Grafana


# ==============
# docker_compose
# --------------
#
# Type: <class 'pathlib.Path'>
# Base Class Info:
#     Required:
#         False
#     Description:
#         The path to the `docker-compose.yml` file.
#     Default value:
#         {DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/docker_compose/docker-compose.yml
# Description:
#     The path to the `docker-compose.yml` file.
# Required:
#     False
# Examples:
#     None


# ==================
# grafana_dashboards
# ------------------
#
# Type: typing.Dict[str, typing.Dict[str, typing.Union[str, int, NoneType]]]
# Description:
#     None
# Required:
#     False
# Examples:
#     None
grafana_dashboards:
  Node Exporter Full:
    id: 1860
    url: https://grafana.com/api/dashboards/1860/revisions/42/download
  cAdvisor Docker Insights:
    id: 19908
    url: https://grafana.com/api/dashboards/19908/revisions/1/download


# ==================
# grafana_admin_user
# ------------------
#
# Type: <class 'str'>
# Description:
#     The Grafana Admin username.
# Required:
#     False
# Examples:
#     None
grafana_admin_user: openstudiolandscapes


# ======================
# grafana_admin_password
# ----------------------
#
# Type: <class 'str'>
# Description:
#     The Grafana Admin password.
# Required:
#     False
# Examples:
#     None
grafana_admin_password: openstudiolandscapes


# ======================
# grafana_port_container
# ----------------------
#
# Type: <class 'int'>
# Description:
#     The Grafana container port.
# Required:
#     False
# Examples:
#     None
grafana_port_container: 3000


# =================
# grafana_port_host
# -----------------
#
# Type: <class 'int'>
# Description:
#     The Grafana host port.
# Required:
#     False
# Examples:
#     None
grafana_port_host: 3030


# ===========================
# grafana_loki_port_container
# ---------------------------
#
# Type: <class 'int'>
# Description:
#     The Grafana Loki container port.
# Required:
#     False
# Examples:
#     None
grafana_loki_port_container: 3100


# ======================
# grafana_loki_port_host
# ----------------------
#
# Type: <class 'int'>
# Description:
#     The Grafana Loki host port.
# Required:
#     False
# Examples:
#     None
grafana_loki_port_host: 3100


# =====================
# grafana_loki_loglevel
# ---------------------
#
# Type: <enum 'GrafanaLogLevel'>
# Description:
#     The Grafana Loki loglevel.
# Required:
#     False
# Examples:
#     ['DEBUG', 'INFO', 'main', 'main_ubuntu', 'version_11_6', 'version_11_6_ubuntu']
grafana_loki_loglevel: info


# =========================
# prometheus_port_container
# -------------------------
#
# Type: <class 'int'>
# Description:
#     The Prometheus container port.
# Required:
#     False
# Examples:
#     None
prometheus_port_container: 9090


# ====================
# prometheus_port_host
# --------------------
#
# Type: <class 'int'>
# Description:
#     The Prometheus host port.
# Required:
#     False
# Examples:
#     None
prometheus_port_host: 9090


# =============
# grafana_image
# -------------
#
# Type: <enum 'GrafanaDockerImage'>
# Description:
#     None
# Required:
#     False
# Examples:
#     ['enterprise', 'oss_legacy', 'oss']
grafana_image: docker.io/grafana/grafana


# =====================
# grafana_image_version
# ---------------------
#
# Type: <enum 'GrafanaDockerImageVersion'>
# Description:
#     None
# Required:
#     False
# Examples:
#     ['latest', 'latest_ubuntu', 'main', 'main_ubuntu', 'version_11_6', 'version_11_6_ubuntu']
grafana_image_version: latest-ubuntu


# ==================
# grafana_loki_image
# ------------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
grafana_loki_image: docker.io/grafana/loki:latest


# ================
# prometheus_image
# ----------------
#
# Type: <class 'str'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
prometheus_image: docker.io/prom/prometheus:main


# ============
# alloy_config
# ------------
#
# Type: <enum 'GrafanaAlloyConfigs'>
# Description:
#     None
# Required:
#     False
# Examples:
#     None
alloy_config: "\n// ###############################\n// #### Metrics Configuration\
  \ ####\n// ###############################\n\n// Host Cadvisor on the Docker socket\
  \ to expose container metrics.\nprometheus.exporter.cadvisor \"example\" {\n  docker_only\
  \ = true\n}\n\ndiscovery.relabel \"example\" {\n  targets = prometheus.exporter.cadvisor.example.targets\n\
  \n  rule {\n    target_label = \"job\"\n    replacement  = \"integrations/docker\"\
  \n  }\n\n  rule {\n    target_label = \"instance\"\n    replacement  = constants.hostname\n\
  \  }\n}\n\n// Configure a prometheus.scrape component to collect cadvisor metrics.\n\
  prometheus.scrape \"scraper\" {\n  targets    = discovery.relabel.example.output\n\
  \  forward_to = [ prometheus.remote_write.demo.receiver ]\n\n  scrape_interval =\
  \ \"10s\"\n}\n\n// Configure a prometheus.remote_write component to send metrics\
  \ to a Prometheus server.\nprometheus.remote_write \"demo\" {\n  endpoint {\n  \
  \  url = \"http://prometheus:9090/api/v1/write\"\n  }\n}\n\ndiscovery.relabel \"\
  metrics\" {\n  targets = prometheus.exporter.unix.metrics.targets\n  rule {\n  \
  \  target_label = \"instance\"\n    replacement = constants.hostname\n  }\n  rule\
  \ {\n    target_label = \"job\"\n    replacement = string.format(\"%s-metrics\"\
  , constants.hostname)\n  }\n}\n\nprometheus.exporter.unix \"metrics\" {\n  disable_collectors\
  \ = [\"ipvs\", \"btrfs\", \"infiniband\", \"xfs\", \"zfs\"]\n  enable_collectors\
  \ = [\"meminfo\"]\n  filesystem {\n    fs_types_exclude = \"^(autofs|binfmt_misc|bpf|cgroup2?|configfs|debugfs|devpts|devtmpfs|tmpfs|fusectl|hugetlbfs|iso9660|mqueue|nsfs|overlay|proc|procfs|pstore|rpc_pipefs|securityfs|selinuxfs|squashfs|sysfs|tracefs)$\"\
  \n    mount_points_exclude = \"^/(dev|proc|run/credentials/.+|sys|var/lib/docker/.+)($|/)\"\
  \n    mount_timeout = \"5s\"\n  }\n  netclass {\n    ignored_devices = \"^(veth.*|cali.*|[a-f0-9]{15})$\"\
  \n  }\n  netdev {\n    device_exclude = \"^(veth.*|cali.*|[a-f0-9]{15})$\"\n  }\n\
  }\n\nprometheus.scrape \"metrics\" {\n  scrape_interval = \"15s\"\n  targets = discovery.relabel.metrics.output\n\
  \  forward_to = [prometheus.remote_write.demo.receiver]\n}\n\n// ###############################\n\
  // #### Logging Configuration ####\n// ###############################\n\n// Discover\
  \ Docker containers and extract metadata.\ndiscovery.docker \"linux\" {\n  host\
  \ = \"unix:///var/run/docker.sock\"\n}\n\n// Define a relabeling rule to create\
  \ a service name from the container name.\ndiscovery.relabel \"docker\" {\n  targets\
  \ = []\n\n  rule {\n    source_labels = [\"__meta_docker_container_name\"]\n   \
  \ regex = \"/(.*)\"\n    target_label = \"container_name\"\n  }\n\n  rule {\n  \
  \  target_label = \"instance\"\n    replacement  = constants.hostname\n  }\n}\n\n\
  // Configure a loki.source.docker component to collect logs from Docker containers.\n\
  loki.source.docker \"docker\" {\n  host       = \"unix:///var/run/docker.sock\"\n\
  \  targets    = discovery.docker.linux.targets\n  relabel_rules = discovery.relabel.docker.rules\n\
  \  forward_to = [loki.write.local.receiver]\n}\n\n// // /var/logs\n// \n// local.file_match\
  \ \"system\" {\n//   path_targets = [\n//     {\n//       __address__ = \"localhost\"\
  ,\n//       __path__ = \"/var/log/*.log\",\n//       job = \"varlogs\",\n//    \
  \ },\n//   ]\n// }\n// \n// loki.source.file \"system\" {\n//   targets = local.file_match.system.targets\n\
  //   forward_to = [\n//     loki.write.local.receiver,\n//   ]\n//   legacy_positions_file\
  \ = \"/tmp/positions.yaml\"\n// }\n\n// journal\n\n// Collect logs from systemd\
  \ journal for node_exporter integration\nloki.source.journal \"journal\" {\n  //\
  \ Only collect logs from the last 24 hours\n  max_age       = \"24h0m0s\"\n  //\
  \ Apply relabeling rules to the logs\n  relabel_rules = discovery.relabel.journal.rules\n\
  \  // Send logs to the local Loki instance\n  forward_to    = [loki.write.local.receiver]\n\
  \  // if alloy is running in container, we \n  // need to add the following path\n\
  \  path = \"/var/log/journal\"\n  labels = {\n    component = string.format(\"%s-journal\"\
  , constants.hostname),\n  }\n}\n\n// Define which log files to collect for node_exporter\n\
  local.file_match \"system\" {\n  path_targets = [{\n    // Target localhost for\
  \ log collection\n    __address__ = \"localhost\",\n    // Collect standard system\
  \ logs\n    __path__ = \"/var/log/{syslog,messages,*.log}\",\n    // Add instance\
  \ label with hostname\n    instance = constants.hostname,\n    // Add job label\
  \ for logs\n    job = string.format(\"%s-logs\", constants.hostname),\n  }]\n}\n\
  \n// Define relabeling rules for systemd journal logs\ndiscovery.relabel \"journal\"\
  \ {\n  targets = []\n\n  rule {\n    // Extract systemd unit information into a\
  \ label\n    source_labels = [\"__journal__systemd_unit\"]\n    target_label  =\
  \ \"unit\"\n  }\n\n  rule {\n    // Extract boot ID information into a label\n \
  \   source_labels = [\"__journal__boot_id\"]\n    target_label  = \"boot_id\"\n\
  \  }\n\n  rule {\n    // Extract transport information into a label\n    source_labels\
  \ = [\"__journal__transport\"]\n    target_label  = \"transport\"\n  }\n\n  rule\
  \ {\n    // Extract log priority into a level label\n    source_labels = [\"__journal_priority_keyword\"\
  ]\n    target_label  = \"level\"\n  }\n}\n\n// Collect logs from files for node_exporter\n\
  loki.source.file \"system\" {\n  // Use targets defined in local.file_match\n  targets\
  \    = local.file_match.system.targets\n  // Send logs to the local Loki instance\n\
  \  forward_to = [loki.write.local.receiver]\n}\n\nloki.write \"local\" {\n  endpoint\
  \ {\n    url = \"http://loki:3100/loki/api/v1/push\"\n  }\n}\n\n// Enable live debugging\
  \ features (empty config means use defaults)\n// - https://grafana.com/docs/alloy/latest/reference/config-blocks/livedebugging/\n\
  // - https://grafana.com/docs/alloy/latest/troubleshoot/debug/\nlivedebugging {\n\
  \  enabled = false\n}\n"
```


</details>


***

# External Resources

> [!CAUTION]
> 
> Starting with Grafana release `12.4.0`,
> the `grafana/grafana-oss` Docker Hub
> repository will no longer be updated.
> Instead, we encourage you to use
> the `grafana/grafana` Docker Hub
> repository. These two repositories
> have the same Grafana OSS docker images.
> 
> ([Source](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/))            

[![Logo Grafana ](https://grafana.com/media/products/cloud/grafana/grafana-product-logo.svg)](https://grafana.com/grafana/)

Grafana is written and maintained by Grafana Labs.

Grafana Labs offers different versions of Grafana:

- OSS
- Enterprise

`OpenStudioLandscapes-Grafana` is based on the [OSS](https://ynput.io/ayon/pricing/) version provided by their own Docker image:

- [`docker.io/grafana/grafana`](https://hub.docker.com/r/grafana/grafana)

## Official Documentation

- [Setup](https://grafana.com/docs/grafana/latest/setup-grafana/)
- [Install](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
- [Configure a Docker Image](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/)
- [Administration](https://grafana.com/docs/grafana/latest/administration/)

### Grafana Alloy

Alloy can collect, process, and export telemetry signals to scale and future-proof your observability approach. More info:

- [https://grafana.com/docs/alloy/latest/](https://grafana.com/docs/alloy/latest/)

#### Alloy Scenarios

This repository contains scenarios that demonstrate how to use Grafana Alloy to monitor various data sources. Each scenario is a self-contained example which will include an LGMT stack (Loki, Grafana, Metrics, Tempo) and an Alloy configuration file.

- [https://github.com/grafana/alloy-scenarios/](https://github.com/grafana/alloy-scenarios/)

## Configure Grafana

### Default Paths

- [Default paths](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/#default-paths)

### `defaults.ini`

As it turned out, the contents of the `defaults.ini` file are tied to the Grafana version. A mismatch can lead to a non-functional container (see [issue](https://github.com/michimussato/OpenStudioLandscapes-Grafana/issues/7)). Hence, the `defaults.ini` file can't be managed by an OpenStudioLandscapes Dagster asset without compromising cross-version compatibility. The main entry point for Grafana configuration is therefore the [`grafana.ini`](#grafanaini) file (exclusively).

### `grafana.ini`

- [Configure Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/)

***

# Community

| Feature                                   | GitHub                                                                                                                                                 | Discord                                                                      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| OpenStudioLandscapes                      | [https://github.com/michimussato/OpenStudioLandscapes](https://github.com/michimussato/OpenStudioLandscapes)                                           | [# openstudiolandscapes-general](https://discord.gg/F6bDRWsHac)              |
| OpenStudioLandscapes-Ayon                 | [https://github.com/michimussato/OpenStudioLandscapes-Ayon](https://github.com/michimussato/OpenStudioLandscapes-Ayon)                                 | [# openstudiolandscapes-ayon](https://discord.gg/gd6etWAF3v)                 |
| OpenStudioLandscapes-Dagster              | [https://github.com/michimussato/OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster)                           | [# openstudiolandscapes-dagster](https://discord.gg/jwB3DwmKvs)              |
| OpenStudioLandscapes-Deadline-10-2        | [https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2)               | [# openstudiolandscapes-deadline-10-2](https://discord.gg/p2UjxHk4Y3)        |
| OpenStudioLandscapes-Deadline-10-2-Worker | [https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2-Worker](https://github.com/michimussato/OpenStudioLandscapes-Deadline-10-2-Worker) | [# openstudiolandscapes-deadline-10-2-worker](https://discord.gg/ttkbfkzUmf) |
| OpenStudioLandscapes-Flamenco             | [https://github.com/michimussato/OpenStudioLandscapes-Flamenco](https://github.com/michimussato/OpenStudioLandscapes-Flamenco)                         | [# openstudiolandscapes-flamenco](https://discord.gg/EPrX5fzBCf)             |
| OpenStudioLandscapes-Flamenco-Worker      | [https://github.com/michimussato/OpenStudioLandscapes-Flamenco-Worker](https://github.com/michimussato/OpenStudioLandscapes-Flamenco-Worker)           | [# openstudiolandscapes-flamenco-worker](https://discord.gg/Sa2zFqSc4p)      |
| OpenStudioLandscapes-Grafana              | [https://github.com/michimussato/OpenStudioLandscapes-Grafana](https://github.com/michimussato/OpenStudioLandscapes-Grafana)                           | [# openstudiolandscapes-grafana](https://discord.gg/gEDQ8vJWDb)              |
| OpenStudioLandscapes-Kitsu                | [https://github.com/michimussato/OpenStudioLandscapes-Kitsu](https://github.com/michimussato/OpenStudioLandscapes-Kitsu)                               | [# openstudiolandscapes-kitsu](https://discord.gg/6cc6mkReJ7)                |
| OpenStudioLandscapes-LikeC4               | [https://github.com/michimussato/OpenStudioLandscapes-LikeC4](https://github.com/michimussato/OpenStudioLandscapes-LikeC4)                             | [# openstudiolandscapes-likec4](https://discord.gg/qAYYsKYF6V)               |
| OpenStudioLandscapes-OpenCue              | [https://github.com/michimussato/OpenStudioLandscapes-OpenCue](https://github.com/michimussato/OpenStudioLandscapes-OpenCue)                           | [# openstudiolandscapes-opencue](https://discord.gg/3DdCZKkVyZ)              |
| OpenStudioLandscapes-OpenCue-Worker       | [https://github.com/michimussato/OpenStudioLandscapes-OpenCue-Worker](https://github.com/michimussato/OpenStudioLandscapes-OpenCue-Worker)             | [# openstudiolandscapes-opencue-worker](https://discord.gg/n9fxxhHa3V)       |
| OpenStudioLandscapes-RustDeskServer       | [https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer](https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer)             | [# openstudiolandscapes-rustdeskserver](https://discord.gg/nJ8Ffd2xY3)       |
| OpenStudioLandscapes-Syncthing            | [https://github.com/michimussato/OpenStudioLandscapes-Syncthing](https://github.com/michimussato/OpenStudioLandscapes-Syncthing)                       | [# openstudiolandscapes-syncthing](https://discord.gg/upb9MCqb3X)            |
| OpenStudioLandscapes-Template             | [https://github.com/michimussato/OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template)                         | [# openstudiolandscapes-template](https://discord.gg/J59GYp3Wpy)             |
| OpenStudioLandscapes-VERT                 | [https://github.com/michimussato/OpenStudioLandscapes-VERT](https://github.com/michimussato/OpenStudioLandscapes-VERT)                                 | [# openstudiolandscapes-vert](https://discord.gg/EPrX5fzBCf)                 |
| OpenStudioLandscapes-filebrowser          | [https://github.com/michimussato/OpenStudioLandscapes-filebrowser](https://github.com/michimussato/OpenStudioLandscapes-filebrowser)                   | [# openstudiolandscapes-filebrowser](https://discord.gg/stzNsZBmwk)          |
| OpenStudioLandscapes-n8n                  | [https://github.com/michimussato/OpenStudioLandscapes-n8n](https://github.com/michimussato/OpenStudioLandscapes-n8n)                                   | [# openstudiolandscapes-n8n](https://discord.gg/yFYrG999wE)                  |

To follow up on the previous LinkedIn publications, visit:

- [OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/company/106731439/).
- [Search for tag #OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23openstudiolandscapes).

***

Last changed: **2026-01-22 09:31:07 UTC**