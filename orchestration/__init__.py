from dagster import Definitions

from .assets import ASSETS
from .jobs import JOBS
from .resources import RESOURCES
from .schedules import SCHEDULES
from .sensors import SENSORS

defs = Definitions(
    assets=ASSETS,
    schedules=SCHEDULES,
    sensors=SENSORS,
    jobs=JOBS,
    resources=RESOURCES,
)
