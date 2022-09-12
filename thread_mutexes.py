from datetime import datetime
from threading import Thread, Lock
from time import sleep

x = 0

mutex = Lock()


def x_value(where):
    print(f"x {where}: {x}")


def thread1():
    global x, mutex
    sleep(3)
    x = 23
    mutex.release()  # released and now other threads with acquire can continue their job


def thread2():
    global x, mutex
    mutex.acquire()  # waiting for release
    sleep(1)
    x = 99


x_value('in start time')
mutex.acquire()  # locking mutex
th1 = Thread(target=thread1)
th2 = Thread(target=thread2)
th1.start()
th2.start()
# Keep notes < x > first must change to 23 then 99
for i in range(20):
    x_value(f'in second {datetime.now().second}')
    sleep(0.25)

x_value('in finish time')
