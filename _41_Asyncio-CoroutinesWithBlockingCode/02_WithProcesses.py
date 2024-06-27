import asyncio
import concurrent.futures

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

async def main(executor, n):
    loop = asyncio.get_running_loop()
    n_factorial = await loop.run_in_executor(executor, factorial, n)
    print(f"The factorial of {n} is {n_factorial}")

if __name__ == '__main__':
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=1)
    n = 25
    try:
        asyncio.run(main(executor, n))
    finally:
        executor.shutdown()
