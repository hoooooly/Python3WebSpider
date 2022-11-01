import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


# 创建任务队列
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task result:', task.result())

# Task result: <Response [200]>
# Task result: <Response [200]>
# Task result: <Response [200]>
# Task result: <Response [200]>
# Task result: <Response [200]>
