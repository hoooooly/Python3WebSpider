"""pip install redis"""

# 推荐使用StructRedis
import time

from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='root')
redis.flushall()  # 清楚所有的键

