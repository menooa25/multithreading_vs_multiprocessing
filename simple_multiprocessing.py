import multiprocessing
import time


def count1(n, t):
    for i in range(1, n+1):
        print(["count1", i])
        time.sleep(t)


def count2(n, t):
    for i in range(1, n+1):
        print(["count2", i])
        time.sleep(t)


for _ in range(1):
    th_count1 = multiprocessing.Process(target=count1, args=(4, 0.2))
    th_count2 = multiprocessing.Process(target=count2, args=(4, 0.4))
    th_count1.start()
    th_count2.start()


# number of active process
print(f"active process: {multiprocessing.active_children()}")
print('done')
