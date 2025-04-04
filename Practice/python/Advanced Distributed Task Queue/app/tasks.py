# app/tasks.py

from celery import Celery
from time import sleep
from app.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery_app.task(name="tasks.long_running_task")
def long_running_task(duration: int):
    """
    Simulate a long running task.
    """
    sleep(duration)
    return f"Task completed in {duration} seconds"
