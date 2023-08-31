from apscheduler.schedulers.blocking import BlockingScheduler
from etl import ETL
from models import models
from settings import get_settings

sched = BlockingScheduler()


@sched.scheduled_job("interval", id="start_etl", minutes=1)
def start_elt():
    for model in models:
        etl = ETL(model)
        etl.try_start()


if __name__ == "__main__":
    start_elt()

    if get_settings().automatic_updates:
        sched.start()
