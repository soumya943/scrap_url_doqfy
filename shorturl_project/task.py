
from celery import shared_task
from shorturl_app.utils import scrape_nifty_data
from .celery import app

@shared_task()
def scrape_nifty_data_task():
    scrape_nifty_data()
