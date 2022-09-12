from celery import Celery

app = Celery('celery_vs_multiprocess_speed', broker='redis://127.0.0.1:6379/1')
app.conf.task_serializer = 'pickle'
app.conf.result_serializer = 'pickle'
app.conf.accept_content = ['application/json', 'application/x-python-serialize']


class CustomTask:
    def __init__(self, name):
        self.name = name


@app.task()
def run_custom_task(custom_task):
    if isinstance(custom_task, CustomTask):
        print(f"This is {custom_task.name}")


run_custom_task.delay(CustomTask('celery'))
