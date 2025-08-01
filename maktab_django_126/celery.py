import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maktab_django_126.settings')

app =  Celery('maktab_django_126')
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()