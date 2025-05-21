
from celery import Celery
from .config import Config

celery = Celery('wpdash', broker=Config.CELERY_BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)
celery.conf.update(task_track_started=True)
