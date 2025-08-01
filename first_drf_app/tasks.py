from maktab_django_126.celery import app
from celery import shared_task

@app.task
def test_task1(a,b):
    return a+b

@shared_task
def test_task2(a,b):
    return a-b