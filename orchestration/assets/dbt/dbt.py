from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from ...constants import DBT_PROJECT


@dbt_assets(manifest=DBT_PROJECT.manifest_path)
def all_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
