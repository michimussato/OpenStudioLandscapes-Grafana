from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Grafana.assets
import OpenStudioLandscapes.Grafana.constants
# from OpenStudioLandscapes.engine.features.upstream_asset_specs import assets_external

assets_base = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Grafana.assets],
)

constants_base = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Grafana.constants],
)


defs = Definitions(
    assets=[
        *assets_base,
        *constants_base,
        # *assets_external,
    ],
)
