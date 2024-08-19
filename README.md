# dagster-dbt-template

This repository serves as a Python project template for building Dagster pipelines with dbt integration.

## Tools

- [rye](https://github.com/astral-sh/rye) project and package manager.
- [sqlfmt](https://github.com/tconbeer/sqlfmt) dbt SQL formatter.

## Usage

1. Install [rye](https://github.com/astral-sh/rye).
2. Clone this repository.
3. Synchronize dependencies.
    ```sh
    rye sync
    ```
4. (Optional) Install recommended Visual Studio Code extensions.
5. Modify the project according to your specific requirements and define your data pipelines.

## Production

For deploying your project to a production environment,
it is recommended to use [Dagster Code Locations](https://docs.dagster.io/concepts/code-locations).
Refer to the provided `Dockerfile` for an example of how to configure your deployment.
