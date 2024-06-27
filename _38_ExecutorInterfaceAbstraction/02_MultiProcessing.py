import multiprocessing, os

def sayhello():
    print(f"Hello from process-{os.getpid()}")
    return

if __name__ == '__main__':
    p = multiprocessing.Process(target=sayhello)
    p.start()
    p.join()
