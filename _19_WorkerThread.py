import threading
import time

def work1(val):
    print("Thread is executing")
    time.sleep(val)
    print("Thread is done executing")

def Method():
    val = 5
    t1 = threading.Thread(target=work1, args=(val,))
    t1. start()

    print("Internal work 1")
    print("Internal work 2")
    t1.join()
    print("Dependent work 1")
    print("Exiting now...")

Method()