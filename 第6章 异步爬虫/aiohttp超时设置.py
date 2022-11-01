import aiohttp
import asyncio


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    data = {'name': 'holy', 'age': 18}
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post('https://httpbin.org/post', json=data) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
