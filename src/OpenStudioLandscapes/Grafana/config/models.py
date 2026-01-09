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

    alloy_config: str = Field(
        default=textwrap.dedent(
            """
            logging {
              level  = "%s"
              format = "logfmt"
            }
            """ % GrafanaLogLevel.INFO
        )
    )


CONFIG_STR = get_config_str(
    Config=Config,
)
