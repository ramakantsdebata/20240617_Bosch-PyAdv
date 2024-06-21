from multiprocessing import Pipe, Process
import random

def make_tuple(conn):
    num = random.randint(1, 9)
    conn.send(('Hi', num))
    print(conn.recv())
    print("Terminating P1")

def make_string(conn):
    tup = conn.recv()
    sub_str, num = tup

    result = ''
    for _ in range(num):
        result += sub_str
    
    conn.send(result)
    print("Terminating P2")


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    p1 = Process(target=make_tuple, args=(conn1,))
    p2 = Process(target=make_string, args=(conn2,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("All done!!")