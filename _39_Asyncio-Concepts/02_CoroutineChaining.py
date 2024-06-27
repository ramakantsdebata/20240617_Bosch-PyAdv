import asyncio

async def perform_task():
    print('performing task')
    print('waiting for result1')
    result1 = await subtask1()
    print('waiting for result2')
    result2 = await subtask2(result1)
    return (result1, result2)

async def subtask1():
    print('perform subtask 1')
    return 'result1'

async def subtask2(arg):
    print('perform subtask2')
    return f'result2 relies on {arg}'

def Main():
    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(perform_task())

    result = asyncio.run(perform_task())

    print(result)

Main()