import asyncio

async def get_item(i):
    await asyncio.sleep(i)
    return f'item {i} completed'

async def main():
    num_items = 5
    item_coros = [get_item(i) for i in range(num_items)]

    print('Starting tasks...')
    for coro in asyncio.as_completed(item_coros):
        result = await coro
        print(result)

# Use asyncio.run() to run the main coroutine
asyncio.run(main())

