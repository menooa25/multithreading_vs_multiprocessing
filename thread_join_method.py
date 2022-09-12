import threading
import time


ln = []


def count1(n, t):
    for i in range(1, n+1):
        ln.append(["count1", i])
        time.sleep(t)


def count2(n, t):
    for i in range(1, n+1):
        ln.append(["count2", i])
        time.sleep(t)


th_count1 = threading.Thread(target=count1, args=(4, 0.2))
th_count2 = threading.Thread(target=count2, args=(4, 0.7))
th_count1.start()
th_count2.start()

th_count1.join()  # waiting for complete th_count1

print(ln)
# number of active threads
print(f"active threads: {threading.active_count()}")
print('done')
