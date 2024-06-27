import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    try:
        async with async_timeout.timeout(10):
            async with session.get(url) as response:
                return await response.text()
    except asyncio.TimeoutError:
        return "Request timed out"

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

# Use asyncio.run() to properly manage the event loop
asyncio.run(main())
