from threading import Semaphore, BoundedSemaphore

def Simplesem():
    # print("Started SimpleSem")
    # time.sleep(1)
    # print("Finished SimpleSem")

    s1 = Semaphore(3)

    print("Acquiring sem 1")
    s1.acquire()
    print("Acquired sem 1")

    print("Acquiring sem 2")
    s1.acquire()
    print("Acquired sem 2")

    print("Acquiring sem 3")
    s1.acquire()
    print("Acquired sem 3")

    s1. release()

    print("Acquiring sem 4")
    s1.acquire()
    print("Acquired sem 4")


    s1.release()
    s1.release()
    s1.release()
    s1.release()

    s1.acquire()
    s1.acquire()
    s1.acquire()
    s1.acquire()

    print("All good till here.")


def BoundedSem():
    s1 = BoundedSemaphore(3)

    try:
        s1.release()
    except Exception as ex:
        print(f"{ex!r}")

def Main():
    Simplesem()
    BoundedSem()

Main()
