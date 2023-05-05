from app import app
from util import fibn_generator
# import tasks
import tasks_inner

@app.task(name="fib_sum")
def fibn_task(*args, **kwargs):
    return tasks_inner.fib_sum(*args, **kwargs)