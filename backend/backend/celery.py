import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
# create a celery instance
app = Celery("backend")
# load the celery configuration
app.config_from_object("django.conf:settings", namespace="CELERY")
# look for celery task
app.autodiscover_tasks()
