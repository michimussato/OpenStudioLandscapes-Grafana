[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Grafana](#feature-openstudiolandscapes-grafana)
   1. [Brief](#brief)
   2. [Requirements](#requirements)
   3. [Install](#install)
      1. [This Feature](#this-feature)
   4. [Add to OpenStudioLandscapes](#add-to-openstudiolandscapes)
   5. [Testing](#testing)
      1. [pre-commit](#pre-commit)
      2. [nox](#nox)
   6. [Variables](#variables)
      1. [Feature Configs](#feature-configs)
2. [Community](#community)
3. [Official Resources](#official-resources)
   1. [Official Documentation](#official-documentation)
      1. [Grafana Alloy](#grafana-alloy)
   2. [Configure Grafana](#configure-grafana)
      1. [Default Paths](#default-paths)
      2. [`defaults.ini`](#defaultsini)
      3. [`grafana.ini`](#grafanaini)

***

This `README.md` was dynamically created with [OpenStudioLandscapesUtil-ReadmeGenerator](https://github.com/michimussato/OpenStudioLandscapesUtil-ReadmeGenerator).

***

# Feature: OpenStudioLandscapes-Grafana

## Brief

This is an extension to the OpenStudioLandscapes ecosystem. The full documentation of OpenStudioLandscapes is available [here](https://github.com/michimussato/OpenStudioLandscapes).

You feel like writing your own Feature? Go and check out the [OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template).

## Requirements

- `python-3.11`
- `OpenStudioLandscapes`

## Install

### This Feature

Clone this repository into `OpenStudioLandscapes/.features`:

```shell
# cd .features
git clone https://github.com/michimussato/OpenStudioLandscapes-Grafana.git
```

Create `venv`:

```shell
# cd .features/OpenStudioLandscapes-Grafana
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools
```

Configure `venv`:

```shell
# cd .features/OpenStudioLandscapes-Grafana
pip install -e "../../[dev]"
pip install -e ".[dev]"
```

For more info see [VCS Support of pip](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Add to OpenStudioLandscapes

Add the following code to `OpenStudioLandscapes.engine.features.FEATURES`:

```python
FEATURES.update(
    "OpenStudioLandscapes-Grafana": {
        "enabled": True|False,
        # - from ENVIRONMENT VARIABLE (.env):
        #   "enabled": get_bool_env("ENV_VAR")
        # - combined:
        #   "enabled": True|False or get_bool_env(
        #       "OPENSTUDIOLANDSCAPES__ENABLE_FEATURE_OPENSTUDIOLANDSCAPES_GRAFANA"
        #   )
        "module": "OpenStudioLandscapes.Grafana.definitions",
        "compose_scope": ComposeScope.DEFAULT,
        "feature_config": OpenStudioLandscapesConfig.DEFAULT,
    }
)
```

## Testing

### pre-commit

- https://pre-commit.com
- https://pre-commit.com/hooks.html

```shell
pre-commit install
```

### nox

#### Generate Report

```shell
nox --no-error-on-missing-interpreters --report .nox/nox-report.json
```

#### Re-Generate this README

```shell
nox -v --add-timestamp --session readme
```

#### Generate Sphinx Documentation

```shell
nox -v --add-timestamp --session docs
```

#### pylint

```shell
nox -v --add-timestamp --session lint
```

##### pylint: disable=redefined-outer-name

- [`W0621`](https://pylint.pycqa.org/en/latest/user_guide/messages/warning/redefined-outer-name.html): Due to Dagsters way of piping arguments into assets.

#### SBOM

Acronym for Software Bill of Materials

```shell
nox -v --add-timestamp --session sbom
```

We create the following SBOMs:

- [`cyclonedx-bom`](https://pypi.org/project/cyclonedx-bom/)
- [`pipdeptree`](https://pypi.org/project/pipdeptree/) (Dot)
- [`pipdeptree`](https://pypi.org/project/pipdeptree/) (Mermaid)

SBOMs for the different Python interpreters defined in [`.noxfile.VERSIONS`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/noxfile.py) will be created in the [`.sbom`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/.sbom) directory of this repository.

- `cyclone-dx`
- `pipdeptree` (Dot)
- `pipdeptree` (Mermaid)

Currently, the following Python interpreters are enabled for testing:

- `python3.11`

## Variables

The following variables are being declared in `OpenStudioLandscapes.Grafana.constants` and are accessible throughout the [`OpenStudioLandscapes-Grafana`](https://github.com/michimussato/OpenStudioLandscapes-Grafana/tree/main/src/OpenStudioLandscapes/Grafana/constants.py) package.

| Variable           | Type   |
| :----------------- | :----- |
| `DOCKER_USE_CACHE` | `bool` |
| `ASSET_HEADER`     | `dict` |
| `FEATURE_CONFIGS`  | `dict` |

### Feature Configs

#### Feature Config: default

| Variable                       | Type   | Value                       |
| :----------------------------- | :----- | :-------------------------- |
| `DOCKER_USE_CACHE`             | `bool` | `False`                     |
| `HOSTNAME`                     | `str`  | `grafana`                   |
| `TELEPORT_ENTRY_POINT_HOST`    | `str`  | `{{HOSTNAME}}`              |
| `TELEPORT_ENTRY_POINT_PORT`    | `str`  | `{{GRAFANA_PORT_HOST}}`     |
| `GRAFANA_ADMIN_USER`           | `str`  | `openstudiolandscapes`      |
| `GRAFANA_ADMIN_PASSWORD`       | `str`  | `openstudiolandscapes`      |
| `GRAFANA_PORT_HOST`            | `str`  | `3030`                      |
| `GRAFANA_PORT_CONTAINER`       | `str`  | `3000`                      |
| `GRAFANA_DOCKER_IMAGE`         | `str`  | `docker.io/grafana/grafana` |
| `GRAFANA_DOCKER_IMAGE_VERSION` | `str`  | `latest-ubuntu`             |

# Community

| Feature                             | GitHub                                                                                                                                     | Discord                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| OpenStudioLandscapes                | [https://github.com/michimussato/OpenStudioLandscapes](https://github.com/michimussato/OpenStudioLandscapes)                               | [# openstudiolandscapes-general](https://discord.gg/F6bDRWsHac)        |
| OpenStudioLandscapes-Ayon           | [https://github.com/michimussato/OpenStudioLandscapes-Ayon](https://github.com/michimussato/OpenStudioLandscapes-Ayon)                     | [# openstudiolandscapes-ayon](https://discord.gg/gd6etWAF3v)           |
| OpenStudioLandscapes-Dagster        | [https://github.com/michimussato/OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster)               | [# openstudiolandscapes-dagster](https://discord.gg/jwB3DwmKvs)        |
| OpenStudioLandscapes-Kitsu          | [https://github.com/michimussato/OpenStudioLandscapes-Kitsu](https://github.com/michimussato/OpenStudioLandscapes-Kitsu)                   | [# openstudiolandscapes-kitsu](https://discord.gg/6cc6mkReJ7)          |
| OpenStudioLandscapes-RustDeskServer | [https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer](https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer) | [# openstudiolandscapes-rustdeskserver](https://discord.gg/nJ8Ffd2xY3) |
| OpenStudioLandscapes-Template       | [https://github.com/michimussato/OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template)             | [# openstudiolandscapes-template](https://discord.gg/J59GYp3Wpy)       |
| OpenStudioLandscapes-Twingate       | [https://github.com/michimussato/OpenStudioLandscapes-Twingate](https://github.com/michimussato/OpenStudioLandscapes-Twingate)             | [# openstudiolandscapes-twingate](https://discord.gg/tREYa6UNJf)       |

To follow up on the previous LinkedIn publications, visit:

- [OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/company/106731439/).
- [Search for tag #OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23openstudiolandscapes).

***

# Official Resources

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