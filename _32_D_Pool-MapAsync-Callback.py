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

def collect_result(result):
    # This function will be called to collect results as they are completed
    results.append(result)
    print(f'Result collected: {result}')

if __name__ == '__main__':
    pool_size = multiprocessing.cpu_count() * 2
    print(f"Spawning {pool_size} processes")
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)

    inputs = list(range(30))
    results = []

    # Use map_async to execute do_work asynchronously
    async_result = pool.map_async(do_work, inputs, callback=collect_result)

    # Wait for all results to be processed
    async_result.wait()

    print(f"Callback_results:, {results}")
    pool.close()  # No more tasks
    pool.join()   # Wait for the worker processes to exit
