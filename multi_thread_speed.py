import psutil
import threading
import time


start_time = time.perf_counter()

start_avaliable_memory = psutil.virtual_memory().available


def print_memory_percentage(status):
    memory_usage = psutil.virtual_memory().percent
    print(f"Memory Percentage in {status}: {memory_usage}%")


def print_cpu_percentage(status):
    memory_usage = psutil.cpu_percent()
    print(f"CPU in {status}: {memory_usage}%")


print_memory_percentage('start')
print_cpu_percentage('start')


def do_somthing():
    time.sleep(1)


threads = []
for _ in range(5000):
    p = threading.Thread(target=do_somthing)
    p.start()
    threads.append(p)


print_memory_percentage('middle of processes')
print_cpu_percentage('middle of processes')

middle_avaliable_memory = psutil.virtual_memory().available


for thread in threads:
    thread.join()

finish_time = time.perf_counter()

print_memory_percentage('finish')
print_cpu_percentage('finish')


print(f'{ round((start_avaliable_memory - middle_avaliable_memory)/1000_000_000,2)}GB increases over 5000 threads')


# number of active process
print(f"Active threads: {threading.active_count()}")
print(f'Done in {round(finish_time - start_time,2)} second(s)')
