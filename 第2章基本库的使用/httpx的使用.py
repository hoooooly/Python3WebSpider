import httpx

"""
    安装
    pip install httpx[http2]


"""

response = httpx.get('https://httpbin.org/get')
print(response.status_code)
print(response.headers)
print(response.text)

"""支持异步请求"""

import asyncio


async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)


if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(fetch('https://httpbin.org/get'))
