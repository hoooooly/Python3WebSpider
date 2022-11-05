import json

import aiohttp
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

'''异步存储MongoDb，需要使用motor库
pip install motor
'''
INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'

PAGE_SIZE = 18
PAGE_NUMBER = 100  # 爬取页码数量
CONCURRENCY = 5  # 并发量

semaphore = asyncio.Semaphore(CONCURRENCY)
session = None


async def scrape_api(url):
    """爬取列表页"""
    async with semaphore:
        try:
            logging.info('开始抓取：%s', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('访问%s发生了错误', url, exc_info=True)


async def scrape_index(page):
    """爬取列表页"""
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)


# 爬取详情页
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_CONNECTION_NAME = 'books'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_CONNECTION_NAME]


async def save_data(data):
    logging.info("保存数据：%s", data)
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)


async def scrape_detail(id_):
    url = DETAIL_URL.format(id=id_)
    data = await scrape_api(url)
    await save_data(data)


# 保存数据


async def main():
    """主方法"""
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER - 1)]
    results = await asyncio.gather(*scrape_index_tasks)
    # logging.info('爬取结果：%s', json.dumps(results, ensure_ascii=False, indent=2))
    # 爬取详情页数据ID
    ids = []
    for index_data in results:
        if not index_data:
            continue
        for item in index_data.get('results'):
            ids.append(item.get('id'))

    # 爬取详情页
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id_)) for id_ in ids]
    await asyncio.wait(scrape_detail_tasks)

    await session.close()  # 抓取完成后关闭会话


if __name__ == '__main__':
    # logging.info('info')
    asyncio.get_event_loop().run_until_complete(main())
