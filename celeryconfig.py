'''
Celery config
'''

BROKER_URL = 'redis://127.0.1:6379/0'
CELERY_BACKEND = 'redis://127.0.1:6379/0'