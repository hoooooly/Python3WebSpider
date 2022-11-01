import aiohttp
import asyncio

CONCURRENCY = 5
URL = 'www.baidu.com'

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api():
    async with semaphore:
        print('scraping', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(100)
            return await response.text()


async def main():
    global session
    session = aiohttp.ClientSession()
    scrap_index_task = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrap_index_task)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
