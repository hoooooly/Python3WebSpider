# 一个分布式的实时文档存储库
# 一个分布式的实时分析搜索引擎

'''
pip install elasticsearch==7.13.0
# 节点和集群
单个 elasticsearch 实例称为一个节点（node），一组节点构成一个集群（cluster）

# 索引
索引即index elasticsearch的顶层单位就叫做索引

# 文档
索引里的单条记录称为文档 document
对于同一个索引里的文档，不要求有相同的结构，但是结构最好保持一致，这样有利于提高搜索效率

# 类型
文档可以分类，文档内的分组叫做类型（type),他是虚拟的逻辑分组

# 字段
每个文档都有类似一个Json结构，包含许多字段，每个字段都有其对应的值
'''

from elasticsearch import Elasticsearch

es = Elasticsearch(
    'http://127.0.0.1:9200',
    verify_certs=False
)
# 创建索引
result = es.indices.create(index='news', ignore=400)
print(result)
# 插入数据
data = {
    'title': '乘风破浪不负韶华',
    'url': 'https://www.baidu.com'
}
result = es.create(index='news', id=1, body=data)
print(result)
# 删除索引
result = es.indices.delete(index='news', ignore=[400, 404])
print(result)
