from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
from celery.signals import after_setup_logger
from keys import *

# Set the default Django settings module for the 'celery' program.
try:
    env = os.environ['APP_ENV']

    raw_env = 'reopt_api.dev_settings'
    # Determine settings based on environment
    if env == 'internal_c110p':
        raw_env = 'reopt_api.internal_c110p_settings'
    elif env == 'development':
        raw_env = 'reopt_api.dev_settings'
    elif env == 'staging':
        raw_env = 'reopt_api.staging_settings'
    elif env == 'production':
        raw_env = 'reopt_api.production_settings'
    else:
        raw_env = 'reopt_api.dev_settings'
except KeyError:
    raw_env = 'reopt_api.dev_settings'

#todo-orr: uncomment before deploy to Prod
os.environ.setdefault('DJANGO_SETTINGS_MODULE','reopt_api.dev_settings')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', raw_env)

app = Celery('reopt_api')

# Use environment variables for configuration
app.config_from_object('django.conf:settings', namespace='CELERY')

# Simplify the Redis configuration
app.conf.broker_url = 'redis://redis:6379/0'

# Create separate queues for each server
app.conf.task_default_queue = os.environ.get('APP_QUEUE_NAME', 'localhost')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    console_formatter = logging.Formatter(
        '%(name)-12s %(levelname)-8s %(filename)s::%(funcName)s line %(lineno)s %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
