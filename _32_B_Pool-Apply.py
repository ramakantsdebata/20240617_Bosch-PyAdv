import multiprocessing
import time

def do_work(data):
    time.sleep(1)  # Simulate some work with sleep
    return data**2

def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    pool_size = multiprocessing.cpu_count() * 2
    print(f"Spawning {pool_size} processes")
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)

    # Use apply to execute do_work synchronously
    result = pool.apply(do_work, args=(10,))
    
    print('Result:', result)
    pool.close()  # No more tasks
    pool.join()   # Wait for the worker processes to exit
