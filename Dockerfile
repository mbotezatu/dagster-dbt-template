ARG PYTHON_VERSION=3.12

FROM docker.io/python:${PYTHON_VERSION}-slim

RUN useradd -u 32768 -g 0 -m -s /bin/sh dagster
USER 32768:0

ENV HOME=/home/dagster
ENV DAGSTER_HOME=${HOME}/.dagster
ENV DAGSTER_CODE_LOCATION=${HOME}/dagster-dbt-template
ENV VIRTUAL_ENV=${DAGSTER_CODE_LOCATION}/.venv
ENV PATH=${VIRTUAL_ENV}/bin:${PATH}

WORKDIR ${DAGSTER_CODE_LOCATION}

COPY --chown=32768:0 ./ ${DAGSTER_CODE_LOCATION}/

ENV PIP_CACHE_DIR=/pip

RUN --mount=type=cache,id=pip,uid=32768,gid=0,dst=/pip \
    python -m venv .venv && \
    .venv/bin/pip install -r requirements.lock && \
    dagster-dbt project prepare-and-package --file orchestration/constants.py

HEALTHCHECK --interval=60s --timeout=30s --start-period=10s --retries=3 \
    CMD [ "dagster", "api", "grpc-health-check", "--host", "0.0.0.0", "--port", "4000" ]

ENTRYPOINT [ "dagster", "api", "grpc" ]

CMD ["--host", "0.0.0.0", "--port", "4000", "--module-name", "orchestration", "--location-name", "dagster-dbt-template"]
