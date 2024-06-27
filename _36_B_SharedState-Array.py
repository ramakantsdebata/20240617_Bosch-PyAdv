import ctypes
from multiprocessing import Array, Lock, Process

def example_function(shared_array, shared_bool_array, shared_long_array):
    with shared_array.get_lock():  # Acquire lock before modifying
        for i in range(len(shared_array)):
            shared_array[i] = i * 2

    # shared_bool was specified without a lock
    for i in range(len(shared_bool_array)):
        shared_bool_array[i] = i % 2 == 0

    # Modify shared_long_array
    with shared_long_array.get_lock():  # Acquire lock before modifying
        for i in range(len(shared_long_array)):
            shared_long_array[i] = i * 3

if __name__ == "__main__":
    shared_array = Array('i', 10)

    shared_bool_array = Array(ctypes.c_bool, 5, lock=False)

    # Shared array of long integers with 8 elements
    shared_long_array = Array('l', 8)

    processes = [Process(target=example_function, args=(shared_array, shared_bool_array, shared_long_array)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("shared_array:", list(shared_array))
    print("shared_bool_array:", list(shared_bool_array))
    print("shared_long_array:", list(shared_long_array))
    