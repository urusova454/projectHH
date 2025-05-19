import os
import time
from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

celery = Celery(
    'worker',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery.task(name="create_task")
def create_task(a,b,c):
    time.sleep(a)
    return b+c
