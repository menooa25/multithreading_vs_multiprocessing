import time
from multiprocessing import Process

from celery import Celery

# docker run -p 6379:6379 redis
app = Celery('celery_vs_multiprocess_speed', broker='redis://127.0.0.1:6379/1')


@app.task
def celery_hard_task():
    number = 90000000
    while number > 0:
        number -= 1
    return "Im celery and the job is done"


def process_hard_task():
    number = 90000000
    while number > 0:
        number -= 1
    return "Im multiprocessing and the job is done"


celery_hard_task.delay()  # This calculates in 2.71s

# multiprocessing takes 2.70s
prs = Process(target=process_hard_task)
start_time = time.time()
prs.start()
prs.join()
finish_time = time.time()
print(finish_time - start_time)
