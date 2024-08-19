from dagster_dbt import DbtCliResource

from ..constants import DBT_PROJECT

RESOURCES = {
    "dbt": DbtCliResource(project_dir=DBT_PROJECT),
}
