from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Grafana.assets
import OpenStudioLandscapes.Grafana.constants
from OpenStudioLandscapes.engine.features.upstream_asset_specs import assets_external

assets = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Grafana.assets],
)

constants = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Grafana.constants],
)


defs = Definitions(
    assets=[
        *assets,
        *constants,
        *assets_external,
    ],
)
