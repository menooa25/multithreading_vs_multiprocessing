import threading
from datetime import datetime
from time import sleep


def time_consume_func(t):
    print('Im time_consume_func and i started')
    sleep(t)
    with open('thread_message.txt', '+a') as f:
        f.write(f"\n Im still alive {datetime.now()}")
    print('Im time_consume_func and i finished')


for _ in range(5):
    th = threading.Thread(target=time_consume_func, args=(3,))
    th.daemon = True
    th.start()
