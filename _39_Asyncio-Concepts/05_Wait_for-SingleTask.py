import asyncio

async def long_running_task(seconds):
    print(f"Task started, will run for {seconds} seconds")
    await asyncio.sleep(seconds)
    return f"Task completed in {seconds} seconds"

async def main():
    try:
        # Run the long_running_task without a timeout
        result = await asyncio.wait_for(long_running_task(3), timeout=None)
        print(result)
    except asyncio.TimeoutError:
        print("The task timed out!")

    try:
        # Run the long_running_task with a timeout of 2 seconds
        result = await asyncio.wait_for(long_running_task(3), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("The task timed out!")

# Use asyncio.run() to run the main coroutine
asyncio.run(main())
