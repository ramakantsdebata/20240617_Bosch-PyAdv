from multiprocessing import Queue, Process
import random
import time


def make_tuple(queue):
    num = random.randint(1, 9)
    queue.put(('Hi', num))
    time.sleep(1)
    print(queue.get())

def make_string(queue):
    tup = queue.get()
    sub_str, num = tup

    result = ''
    for _ in range(num):
        result += sub_str
    
    queue.put(result)


if __name__ == '__main__':
    queue = Queue()
    p1 = Process(target=make_tuple, args=(queue,))
    p2 = Process(target=make_string, args=(queue,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("All done!!")