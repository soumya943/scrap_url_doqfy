import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shorturl_project.settings")

app = Celery('shorturl_project',include=['shorturl_project.task'])
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'Asia/Kolkata'

if __name__ == '__main__':
    app.start()
