"""

TODO I'll use the tasks to run experiments.

"""


import redis
import celery

# Chaining
from celery import Celery, chain

app = Celery('fibonacci', broker='redis://localhost',
             backend="redis://localhost")

from tasks import *
