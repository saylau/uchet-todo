import os
import sys

from celery import Celery
from configurations.management import execute_from_command_line

# set the default Django settings module for the 'celery' program.
if not ("DJANGO_SETTINGS_MODULE" in os.environ):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    execute_from_command_line(sys.argv)

app = Celery("uchet-todo")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
