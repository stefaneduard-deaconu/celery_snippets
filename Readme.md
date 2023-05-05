# Using Celery with Redis 

## Setting up

Installing celery and redis

1. `pip install celery celery[redis]`
2. Also install redis -> insert tutorial link
3. Check with systemctl status redis-server    or    redis-cli ping (response should be PONG)

## Steps to run:

1. Start a celery worker:
    
    ```sh
bash run_celery_single_worker.sh
    ```

2. Run tests using unittest, inside 


1\. uses cleery -A app worker to create a single worker

## AsyncResult

```python
a = hard_task.delay(999, "Moon landing")
a.status
a.result  # this is the return value of the difficult task ;)
```