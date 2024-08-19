from dagster import load_assets_from_package_module

from ..constants import DBT_GROUP_NAME
from . import dbt

ASSETS = [
    *load_assets_from_package_module(dbt, group_name=DBT_GROUP_NAME),
]
