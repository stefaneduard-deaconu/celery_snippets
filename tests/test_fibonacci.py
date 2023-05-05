import subprocess
import time

import unittest


class CeleryRedisTest(unittest.TestCase):
    def setUp(self) -> None:
        # TODO Ed, replace with running containers?
        # start redis-server
        while True:
            ping_answer = subprocess.run(['redis-cli', 
                                          'ping'],
                                         capture_output=True, text=True)
            try:
                print(ping_answer.stdout)
                assert ping_answer.stdout.strip() == 'PONG'
                break
            except:
                breakpoint()
                status_out = subprocess.run(["sudo",
                                             "service",
                                             "redis-server",
                                             "status"])
        # start celery
        subprocess.run(['python', ''])

import tasks

class TestFibonacci(CeleryRedisTest):
    def setUp(self) -> None:
        super().setUp()
    
    def test_simple(self):
        res = tasks.fib_sum.delay(5)  # 1 + 1 + 2 + 3 + 5
        while res.status == 'PENDING':
            time.sleep(1)
        assert res.result == 12

    def test_grouped(self):
        res = tasks.fib_sum.delay(5)  # 1 + 1 + 2 + 3 + 5
        while res.status == 'PENDING':
            time.sleep(1)
        assert res.result == 12
