[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Grafana](#feature-openstudiolandscapes-grafana)
   1. [Brief](#brief)
   2. [Clone](#clone)
      1. [Clone and Install](#clone-and-install)
   3. [Configure](#configure)
      1. [Default Configuration](#default-configuration)
   4. [Local Development/Unit Testing/Debugging](#local-developmentunit-testingdebugging)
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

## Clone

Clone this repository into `OpenStudioLandscapes/.features` (assuming the current working directory to be the Git repository root `./OpenStudioLandscapes`):

```shell
# cd OpenStudioLandscapes
source .venv/bin/activate
openstudiolandscapes clone-feature --repo=https://github.com/michimussato/OpenStudioLandscapes-Grafana.git
deactivate
# Check the resulting console output for installation instructions
```

### Clone and Install

```shell
# cd OpenStudioLandscapes
source .venv/bin/activate
openstudiolandscapes clone-feature --repo=https://github.com/michimussato/OpenStudioLandscapes-Grafana.git \
    && pip install --editable ./.features/OpenStudioLandscapes-Grafana
deactivate
```

For more info on `pip` see [VCS Support of `pip`](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Configure

OpenStudioLandscapes will search for a local config store. The default location is `~/.config/OpenStudioLandscapes/config-store/` but you can specify a different location if you need to.

> [!TIP]
> 
> To specify a config store location different from
> the default location, check out the OpenStudioLandscapes 
> [CLI Section](https://github.com/michimussato/OpenStudioLandscapes#cli)
> to find out how to do that.

A local config store location will be created if it doesn't exist, together with the `config.yml` files for each individual Feature.

> [!TIP]
> 
> The config store root will be initialized as a local Git
> controlled repository. This makes it easy to track changes
> you made to the `config.yml`.

The following settings are available in `OpenStudioLandscapes-Grafana` and are based on [`OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/config/models.py`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/config/models.py).

### Default Configuration

<details open>
<summary><code>config.yml</code></summary>


```yaml
$defs:
  GrafanaDockerImage:
    enum:
    - docker.io/grafana/grafana-enterprise
    - docker.io/grafana/grafana-oss
    - docker.io/grafana/grafana
    title: GrafanaDockerImage
    type: string
  GrafanaDockerImageVersion:
    enum:
    - latest
    - latest-ubuntu
    - main
    - main-ubuntu
    - '11.6'
    - 11.6-ubuntu
    title: GrafanaDockerImageVersion
    type: string
  GrafanaLogLevel:
    enum:
    - debug
    - info
    - main
    - main-ubuntu
    - '11.6'
    - 11.6-ubuntu
    title: GrafanaLogLevel
    type: string
properties:
  GF_PATHS_DATA:
    default: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/var/lib/grafana'
    format: path
    title: Gf Paths Data
    type: string
  alloy_apt_packages:
    default:
    - zfsutils-linux
    items:
      type: string
    title: Alloy Apt Packages
    type: array
  alloy_image:
    default: docker.io/grafana/alloy:latest
    title: Alloy Image
    type: string
  compose_scope:
    default: default
    examples:
    - default
    - license_server
    - worker
    title: Compose Scope
    type: string
  docker_compose:
    default: '{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/docker_compose/docker-compose.yml'
    description: The path to the `docker-compose.yml` file.
    format: path
    title: Docker Compose
    type: string
  enabled:
    default: true
    description: Whether the Feature is enabled or not.
    title: Enabled
    type: boolean
  endpoint_loki:
    default: http://loki
    title: Endpoint Loki
    type: string
  endpoint_prometheus:
    default: http://prometheus
    title: Endpoint Prometheus
    type: string
  env:
    additionalProperties: true
    title: Env
    type: object
  feature_name:
    default: OpenStudioLandscapes-Grafana
    title: Feature Name
    type: string
  grafana_admin_password:
    default: openstudiolandscapes
    description: https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#admin_password
    title: Grafana Admin Password
    type: string
  grafana_admin_user:
    default: openstudiolandscapes
    description: https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#admin_user
    title: Grafana Admin User
    type: string
  grafana_dashboards:
    additionalProperties:
      additionalProperties:
        anyOf:
        - type: string
        - type: integer
        - type: 'null'
      type: object
    default:
      Node Exporter Full:
        id: 1860
        url: https://grafana.com/api/dashboards/1860/revisions/42/download
      cAdvisor Docker Insights:
        id: 19908
        url: https://grafana.com/api/dashboards/19908/revisions/1/download
    title: Grafana Dashboards
    type: object
  grafana_image:
    $ref: '#/$defs/GrafanaDockerImage'
    default: docker.io/grafana/grafana
    examples:
    - enterprise
    - oss_legacy
    - oss
  grafana_image_version:
    $ref: '#/$defs/GrafanaDockerImageVersion'
    default: latest-ubuntu
    examples:
    - latest
    - latest_ubuntu
    - main
    - main_ubuntu
    - version_11_6
    - version_11_6_ubuntu
  grafana_loki_image:
    default: docker.io/grafana/loki:latest
    title: Grafana Loki Image
    type: string
  grafana_loki_loglevel:
    $ref: '#/$defs/GrafanaLogLevel'
    default: info
    description: The Grafana Loki loglevel.
    examples:
    - DEBUG
    - INFO
    - main
    - main_ubuntu
    - version_11_6
    - version_11_6_ubuntu
  grafana_loki_port_container:
    default: 3100
    description: The Grafana Loki container port.
    exclusiveMinimum: 0
    title: Grafana Loki Port Container
    type: integer
  grafana_loki_port_host:
    default: 3100
    description: The Grafana Loki host port.
    exclusiveMinimum: 0
    title: Grafana Loki Port Host
    type: integer
  grafana_port_container:
    default: 3000
    description: The Grafana container port.
    exclusiveMinimum: 0
    title: Grafana Port Container
    type: integer
  grafana_port_host:
    default: 3030
    description: The Grafana host port.
    exclusiveMinimum: 0
    title: Grafana Port Host
    type: integer
  grafana_root_url:
    default: http://localhost:3000
    description: https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#root_url
    title: Grafana Root Url
    type: string
  group_name:
    default: OpenStudioLandscapes_Grafana
    title: Group Name
    type: string
  key_prefixes:
    default:
    - OpenStudioLandscapes_Grafana
    items:
      type: string
    title: Key Prefixes
    type: array
  local_bind_volumes:
    description: Here you can define Feature specific, arbitrary, absolute bind volume
      mappings.
    items:
      type: string
    title: Local Bind Volumes
    type: array
  local_environment_variables:
    additionalProperties:
      type: string
    description: Here you can define Feature specific, arbitrary environment variables.
    title: Local Environment Variables
    type: object
  prometheus_image:
    default: docker.io/prom/prometheus:main
    title: Prometheus Image
    type: string
  prometheus_port_container:
    default: 9090
    description: The Prometheus container port.
    exclusiveMinimum: 0
    title: Prometheus Port Container
    type: integer
  prometheus_port_host:
    default: 9090
    description: The Prometheus host port.
    exclusiveMinimum: 0
    title: Prometheus Port Host
    type: integer
title: Config
type: object

```

</details>


## Local Development/Unit Testing/Debugging

This is for isolated development, unit testing and debugging. Instead of the [`OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/definitions.py`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/definitions.py), the accompanying [`OpenStudioLandscapes-Grafana/tree/main/workspace.yaml`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/workspace.yaml) loads the [`OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/_definitions_with_upstream_specs.py`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/_definitions_with_upstream_specs.py) which also contains [`AssetSpec`](https://release-1-9-13.archive.dagster-docs.io/api/dagster/assets#dagster.AssetSpec) definitions for upstream dependencies as [external assets](https://release-1-9-13.archive.dagster-docs.io/guides/build/assets/external-assets).

```shell
# cd ./.features/OpenStudioLandscapes-Grafana
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools setuptools_scm wheel
pip install --editable .[dev]
dagster dev --workspace workspace.yaml
```

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

Last changed: **2026-05-07 19:21:24 UTC**