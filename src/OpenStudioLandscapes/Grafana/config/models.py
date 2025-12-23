import enum
import pathlib

from dagster import get_dagster_logger
from pydantic import (
    Field,
    PositiveInt,
)

LOGGER = get_dagster_logger(__name__)

from OpenStudioLandscapes.engine.config.str_gen import get_config_str
from OpenStudioLandscapes.engine.config.models import FeatureBaseModel

from OpenStudioLandscapes.Grafana import dist

config_default = pathlib.Path(__file__).parent.joinpath("config_default.yml")


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


class Config(FeatureBaseModel):

    feature_name: str = dist.name

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

    grafana_image: GrafanaDockerImage = Field(
        default=GrafanaDockerImage.oss,
        examples=[i.name for i in GrafanaDockerImage],
    )

    grafana_image_version: GrafanaDockerImageVersion = Field(
        default=GrafanaDockerImageVersion.latest_ubuntu,
        examples=[i.name for i in GrafanaDockerImageVersion],
    )


CONFIG_STR = get_config_str(
    Config=Config,
)

