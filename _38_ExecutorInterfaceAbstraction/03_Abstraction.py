from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def sayhello(name):
    print(f"Hello from {name}")
    return

if __name__ == '__main__':
    # Thread executor
    executor1 = ThreadPoolExecutor(max_workers=2)
    futures = [executor1.submit(sayhello, f"Thread {("Manish's Thread", "Abhijeet's Thread")[i]}") for i in range(2)]
    for future in futures:
        future.result()
    executor1.shutdown(wait=True)

    # Process executor
    executor2 = ProcessPoolExecutor(max_workers=2)
    futures = [executor2.submit(sayhello, f"Process {("Pravin's Process", "Ramakant's Process")[i]}") for i in range(2)]
    for future in futures:
        future.result()
    executor2.shutdown(wait=True)
