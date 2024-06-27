import threading

def sayhello():
    print(f"Hello from {threading.current_thread().name}")
    return

p = threading.Thread(target=sayhello)
p.start()
p.join()
