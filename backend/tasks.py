
from .celery_app import celery
import requests

@celery.task
def ping_site(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code
    except Exception as e:
        return str(e)
