from app import app
from util import fibn_generator

def fib_sum(n: int):
    return sum(fibn_generator(n))