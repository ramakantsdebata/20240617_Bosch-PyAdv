from threading import Thread
from queue import Queue
from random import randint, uniform
import time

def producer(queue):
    for i in range(10):
        time.sleep(uniform(0.1, 0.5)) # Simulate production time
        item = randint(11, 20)
        print(f"Produced put: '{item}' in queue")
        queue.put(item)
    print("Producer: poisoning the queue.")
    queue.put(None) # Poison Pill

def consumer(queue):
    while(True):
        item = queue.get()
        if item is None:
            print("Consumer: Nothing more to wait for")
            break
        print(f"Consumer get: '{item}' from the queue")
        queue.task_done() # Mark item as done()
        time.sleep(uniform(0.1, 0.5)) # Simulate consumption time

if __name__ == '__main__':
    queue = Queue()

    t1 = Thread(target=producer, args=(queue,))
    t2 = Thread(target=consumer, args=(queue,))

    t1.start(); t2.start()

    t1.join(); t2.join()

    print("All done.")