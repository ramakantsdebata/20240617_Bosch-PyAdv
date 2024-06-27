import asyncio
import aiofiles

# asyncio way of filehandling; 
# benefit is that the CPU is relinquished back to the event_loop, when IO is being performed
async def main():
    async with aiofiles.open('file.txt', mode='w') as f:
        await f.write('data')

    async with aiofiles.open('file.txt', mode='r') as f:
        contents = await f.read()
    print(contents)

asyncio.run(main())

