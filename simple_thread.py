import threading
import time


def count1(n, t):
    for i in range(1, n+1):
        print(f"count1: {i}")
        time.sleep(t)


def count2(n, t):
    for i in range(1, n+1):
        print(f"count2: {i}")
        time.sleep(t)


for _ in range(2):
    th_count1 = threading.Thread(target=count1, args=(4, 0.4))
    th_count2 = threading.Thread(target=count1, args=(4, 0.2))
    th_count1.start()
    th_count2.start()


# number of active threads
print(f"active threads: {threading.active_count()}")
print('done')
