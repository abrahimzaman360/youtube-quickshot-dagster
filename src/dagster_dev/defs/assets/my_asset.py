import dagster as dg

print("""
This is a test asset!
Please do not focus on it...
""")


@dg.asset
def my_asset(context: dg.AssetExecutionContext) -> dg.MaterializeResult:
    return dg.MaterializeResult(
        metadata={
            "my_metadata": "my_value",
        },
    )
