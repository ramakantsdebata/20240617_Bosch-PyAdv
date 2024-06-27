from multiprocessing import Manager, Process

def worker(shared_dict, shared_list):
    shared_dict['count'] += 1
    shared_list.append(shared_dict['count'])

if __name__ == "__main__":
    manager = Manager()                         # Starts the server process, where the data objects will be created and shared from
    
    shared_dict = manager.dict({'count': 0})    # Creates a dict object on the server process and returns a proxy of it
    shared_list = manager.list()                # Creates a list object on the server process and returns a proxy of it
    
    processes = []
    for _ in range(5):
        p = Process(target=worker, args=(shared_dict, shared_list))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print("Final shared_dict:", dict(shared_dict))
    print("Final shared_list:", list(shared_list))
