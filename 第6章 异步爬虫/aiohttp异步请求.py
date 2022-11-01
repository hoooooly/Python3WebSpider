import asyncio

import aiohttp
import requests
import time

"""pip install aiohttp"""

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    resopnse = await session.get(url)
    await resopnse.text()
    await session.close()
    return resopnse


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'respone', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
