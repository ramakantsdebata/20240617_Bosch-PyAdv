import multiprocessing
import time

def do_work():
    print('Starting do_work function')
    time.sleep(5)
    print('Finished do_work function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=do_work)
    print(f"[Before Start] Process is alive: {p.is_alive()}")
    p.start()
    print(f"[Running] Process is alive: {p.is_alive()}")
    p.terminate()
    p.join()
    print(f"[After Termination] Process is alive: {p.is_alive()}")
    print(f"Process exit code: {p.exitcode}")
