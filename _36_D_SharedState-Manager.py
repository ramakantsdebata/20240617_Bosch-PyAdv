from audioop import mul
import multiprocessing

def do_work(dictionary, item):
    dictionary[item] = item ** 2

if __name__ == '__main__':
    mgr = multiprocessing.Manager()     # Starts the server process
    d = mgr.dict()                      # Creates a dict object on the server process and returns a proxy of it

    jobs = [multiprocessing.Process(target=do_work, args=(d, i)) for i in range(8)]     # Pass the dict() proxy to the processes

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print('Results:', d)