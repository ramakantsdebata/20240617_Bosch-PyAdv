import threading


def worker():
    print("Executing the job")

def main():
    print("Starting main")

    t1 = threading.Timer(5.0, worker)
    t1.start()

main()