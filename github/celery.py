from __future__ import absolute_import

from celery import Celery

celery = Celery('github', include=['github.tasks'])
celery.config_from_object('celeryconfig')

celery.conf.update(
    CELERY_RESULT_SERIALIZER='json',
    CELERY_TASK_SERIALIZER='json',

    CELERY_TASK_RESULT_EXPIRES=60,

    CELERY_DEFAULT_QUEUE="github",
    CELERY_DEFAULT_EXCHANGE="github",

    CELERY_RESULT_EXCHANGE = "github",
    CELERY_DEFAULT_ROUTING_KEY = 'github'
)