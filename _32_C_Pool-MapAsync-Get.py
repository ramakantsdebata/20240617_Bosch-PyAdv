'''
map_async(func, iterable[, chunksize[, callback]]) returns AsyncResult
'''

import multiprocessing
import time

def do_work(data):
    time.sleep(1)
    return data**2

def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    pool_size = multiprocessing.cpu_count() * 2
    print(f"Spawning {pool_size} processes")
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)

    inputs = list(range(30))

    # Use map_async to execute do_work asynchronously
    async_result = pool.map_async(do_work, inputs)

    # Fetch the results
    outputs = async_result.get()

    print('Outputs:', outputs)
    pool.close()  # No more tasks
    pool.join()   # Wait for the worker processes to exit
