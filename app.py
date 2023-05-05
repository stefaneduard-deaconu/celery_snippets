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
# def client1():
#     # 2 + 2 + 4 + 8
#     res = chain(add.s(2,2), add.s(4), add.s(8))
#     return res.get()
# 
# def client2():
#     res = (add.s(2,2) | add.s(4) | add.s(8))()
#     return res.get()
