import aiohttp
import asyncio


async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.httpbin.org/get', params=params) as response:
            print(await response.text())


async def main1():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.httpbin.org/get', data=data) as response:
            print(await response.text())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main1())
