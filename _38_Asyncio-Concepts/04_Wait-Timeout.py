## Timeout before all tasks complete
import asyncio

async def get_item(i):
    await asyncio.sleep(i)
    return 'item' + str(i)

async def get_items(num_items):
    print('getting items')
    item_tasks = [asyncio.ensure_future(get_item(i)) for i in range(num_items)]
    print("waiting 2 seconds for tasks' run")
    completed, pending = await asyncio.wait(item_tasks, timeout=2)
    results = [t.result() for t in completed]
    print(f'results: {results!r}')
    if pending:
        print('cancelling remaining tasks')
        for t in pending:
            t.cancel()

# Use asyncio.run() to properly manage the event loop
asyncio.run(get_items(4))
