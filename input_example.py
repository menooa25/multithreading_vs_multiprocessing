import threading, multiprocessing
import time


class Operation:
    def __init__(self, name):
        self.name = name


def multi_task_func(inp):
    time.sleep(3)
    print(f'im {inp.name} and im done')


th = threading.Thread(target=multi_task_func, args=(Operation("multithreading"),))
prs = multiprocessing.Process(target=multi_task_func, args=(Operation('multiprocessing'),))

th.start()
prs.start()

print('done')
