# scraper/tasks.py

from celery import shared_task
from .utils import scrape_nifty_data

@shared_task
def scrape_nifty_data_task():
    scrape_nifty_data()
