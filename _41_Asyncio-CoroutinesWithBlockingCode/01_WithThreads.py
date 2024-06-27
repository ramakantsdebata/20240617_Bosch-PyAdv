import time
import asyncio
import concurrent.futures

def blocking_func(n):
    time.sleep(0.5)
    return n ** 2

async def main(executor):
    loop = asyncio.get_running_loop()
    print('creating executor tasks')
    blocking_tasks = [
        loop.run_in_executor(executor, blocking_func, i)
        for i in range(6)
    ]
    print('waiting for tasks to complete')
    results = await asyncio.gather(*blocking_tasks)
    print(f'results: {results!r}')

if __name__ == '__main__':
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    try:
        asyncio.run(main(executor))
    finally:
        executor.shutdown()
