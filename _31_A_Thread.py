import threading

def do_some_work(val):
    print("doing some work in thread")
    print(f"echo: {val}")
    return

val = "text"
t = threading.Thread(target=do_some_work, args=(val,))
t.start()
t.join()