import threading
import time

def worker(event):
    print("Wating for the evernt...")
    event.wait()
    print("Received event")

def main():
    print("Starting main")
    event = threading.Event()

    t1 = threading.Thread(target=worker, args=(event,))
    t1.start()
    print("Event not ready yet.")
    time.sleep(5)
    print("Event ready. Singnalling now...")
    event.set()

    t1.join()
    event.clear()
    
    print("Thread is back on track")

main()