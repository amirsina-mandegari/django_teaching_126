from celery import Celery
import time

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(a,b):
    print('sleep for 10 seconds')
    time.sleep(10)
    return a+b

# print(add(2,3))