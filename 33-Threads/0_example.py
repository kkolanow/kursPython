import threading
from threading import Thread

import time


def execute_slowly(name,lock):
    acquire = lock.acquire()
    print('start thread number '+str(name))
    for i in range(10, 0, -1):
        print("ThreadNo: "+str(name) + " , value:" + str(i))
        time.sleep(1)
    print('end thread number: ' + str(name))
    lock.release()

lock = threading.Lock()
for t in range(10):
    try:
        t = Thread(target=execute_slowly, args=((t,lock)))
        t.start()
    except Exception as err:
        print("Failed with error: ", str(err))


for thread in threading.enumerate():
    print(thread.name)


