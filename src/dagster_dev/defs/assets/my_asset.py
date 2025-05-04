import dagster as dg


@dg.asset
def my_asset(context: dg.AssetExecutionContext) -> dg.MaterializeResult:
    return dg.MaterializeResult(
        metadata={
            "my_metadata": "my_value",
        },
    )
