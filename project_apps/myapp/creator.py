from apscheduler.schedulers.background import BackgroundScheduler
from myapp.cron import my_cron_job


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_cron_job, "interval", minutes=1)
    scheduler.start()
