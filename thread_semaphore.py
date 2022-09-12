from threading import Thread, Semaphore
from time import sleep

database_connections = []
semaphore = Semaphore(3)


def connection(_id):
    semaphore.acquire()
    connection_name = f"connection_{_id}"
    database_connections.append(connection_name)
    sleep(0.5)
    database_connections.remove(connection_name)
    semaphore.release()


for i in range(1, 50):
    th = Thread(target=connection, args=(i,))
    th.start()


for _ in range(35):
    print(database_connections)
    sleep(0.25)
