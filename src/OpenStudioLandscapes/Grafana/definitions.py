from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Grafana.assets
from OpenStudioLandscapes.Grafana import (
    LOGGER,
    dist,
)

LOGGER.info(f"Loading {dist.name} assets...")

assets_base = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Grafana.assets],
)

defs = Definitions(
    assets=[
        *assets_base,
    ],
)
