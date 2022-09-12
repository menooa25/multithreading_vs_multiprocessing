import multiprocessing
from time import sleep


def time_consuming_func(t):
    print('Im time consuming and i started')
    sleep(t)
    print('Im time consuming and i finished')


for _ in range(10):
    prs = multiprocessing.Process(target=time_consuming_func, args=(3,))
    prs.start()


# killing process with object method
# for process in multiprocessing.active_children():
#     process.terminate()


# killing with process id
def kill_process(_id):
    child_process = [p for p in multiprocessing.active_children() if p.pid == _id]
    child_process[0].terminate() if child_process else _


for process in multiprocessing.active_children():
    process_id = process.pid
    kill_process(process_id)
