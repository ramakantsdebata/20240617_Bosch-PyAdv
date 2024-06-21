import multiprocessing
import time

def do_work(data):
    time.sleep(1)
    return data**2

def start_process():
    print('Starting', multiprocessing.current_process().name)
    
if __name__ == '__main__':
    pool_size= multiprocessing.cpu_count() * 2
    print(f"Spawning {pool_size} processes")
    pool = multiprocessing.Pool(processes=pool_size,
                                initializer=start_process)
    inputs = list(range(30))
    outputs = pool.map(do_work, inputs)
    print('Outputs :', outputs)
    pool.close() # no more tasks
    pool.join() # wait for the worker processes to exit
