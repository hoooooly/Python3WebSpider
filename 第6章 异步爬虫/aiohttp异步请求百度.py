import asyncio

import aiohttp
import requests
import time

"""pip install aiohttp"""


def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        resopnse = await session.get(url)
        await resopnse.text()
        await session.close()
        return resopnse

    async def request():
        url = 'https://www.baidu.com/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print('Number:', number, 'Cost time:', end - start)


for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)
