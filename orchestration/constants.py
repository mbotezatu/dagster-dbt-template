from pathlib import Path

from dagster_dbt import DbtProject

DBT_GROUP_NAME = "dbt"
DBT_PROJECT_DIR = Path(__file__).joinpath("..", "..").resolve()
DBT_PROJECT = DbtProject(
    project_dir=DBT_PROJECT_DIR,
)
DBT_PROJECT.prepare_if_dev()
