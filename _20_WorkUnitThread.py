import threading
import time

class MyThread(threading.Thread):
    def __init__(self, value):
        super().__init__()
        self.val = value

    def run(self):
        print("Thread is executing")
        time.sleep(self.val)
        print("Thread is done executing")

def Method():
    val = 5

    t1 = MyThread(val)
    t1.start()
    print("Internal work 1")

    print("Internal work 2")

    t1.join()

    print("Dependent work 1")

    print("Exiting now...")

Method()