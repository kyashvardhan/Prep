# app/celery_worker.py

from app.tasks import celery_app

if __name__ == "__main__":
    # Launch the Celery worker from the command line.
    celery_app.worker_main(["worker", "--loglevel=info"])
