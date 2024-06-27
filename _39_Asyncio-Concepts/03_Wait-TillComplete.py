## Waiting for all tasks to complete
import asyncio

async def get_item(i):
    await asyncio.sleep(i)
    return 'item' + str(i)

async def get_items(num_items):
    print('getting items')
    item_tasks = [asyncio.ensure_future(get_item(i)) for i in range(num_items)]
    print('waiting for tasks to complete')
    completed, pending = await asyncio.wait(item_tasks)
    # pending will be empty here; Ignore it.
    results = [t.result() for t in completed]
    print(f'results: {results!r}')

# Use asyncio.run() to properly manage the event loop
asyncio.run(get_items(4))
