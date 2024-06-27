import os
import threading
import time
import random

def producer(write_pipe):
    for _ in range(5):
        item = random.randint(1, 100)
        print(f'Producer: producing item {item}')
        os.write(write_pipe, f"{item}\n".encode())
        time.sleep(random.uniform(0.1, 0.5))
    # Signal to consumer that production is done
    os.write(write_pipe, b"None\n")
    os.close(write_pipe)

def consumer(read_pipe):
    while True:
        item = os.read(read_pipe, 1024).decode().strip()
        if item == "None":
            break
        print(f'Consumer: consuming item {item}')
        time.sleep(random.uniform(0.1, 0.5))
    os.close(read_pipe)

def main():
    read_pipe, write_pipe = os.pipe()

    t1 = threading.Thread(target=producer, args=(write_pipe,))
    t2 = threading.Thread(target=consumer, args=(read_pipe,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
