import threading
import time

barrier = threading.Barrier(3)


class thread(threading.Thread):
    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID

    def run(self):
        print("Setting: "+ str(self.thread_ID) + "\n")
        barrier.wait()
        print(str(self.thread_ID) + 'Release >>>>>> FLUSH')


thread1 = thread(100)
thread2 = thread(101)

thread1.start()
thread2.start()
print('Threads started, but barrier not reached yet!')
time.sleep(2)

print('Call barier third time to release it')
barrier.wait()

print("Exit\n")
