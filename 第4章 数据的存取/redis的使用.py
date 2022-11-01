"""pip install redis"""

# 推荐使用StructRedis
import time

from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='root')
redis.set('name', 'Holy')
redis.set('nike', 'Good')
redis.set('age', 10)
print(redis.get('name'))

# 键操作
# 判断一个键是否存在
print(redis.exists('name'))  # 1
# 删除一个键
print(redis.delete('age'))  # 1
# 判断键的类型
print(redis.type('name'))  # b'string'
# 获取符合规则的键
print(redis.keys('n*'))  # [b'name', b'nike']
# 随机获取一个键
print(redis.randomkey())
# 对键重命名
redis.rename('nike', 'Nike')
print(redis.get('Nike'))  # b'Good'
# 获取当前数据库中键的数量
print(redis.dbsize())  # 2
# 设置键的过期时间
redis.set('twoSec', 2)
print(redis.get('twoSec'))  # b'2'
redis.expire('twoSec', 2)
time.sleep(3)
print(redis.get('twoSec'))  # None
# 获取键的过期时间，-1 表示永不过期
print(redis.ttl('name')) # -1
# 将键移到其他数据库
redis.move('name', 2)
# 删除当前数据库中的所有键
redis.flushdb()
# 删除所有数据库中的所有键
redis.flushall()
