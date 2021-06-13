from celery import Celery

celery_app = Celery(
    broker='pyamqp://guest@localhost//',
)