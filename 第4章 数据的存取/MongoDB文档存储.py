"""pip install pymongo"""
import pymongo

# 连接
client = pymongo.MongoClient(host='localhost', port=27017)
# 也可以传入mongodb://localhost:27017
# client = pymongo.MongoClient(mongodb://localhost:27017)

# 指定数据库，MongoDB可以创建多个数据库
db = client.test
# 也可以 db = client['test']

# 指定集合 也可以 collecction = db['students']
collection = db.students

# 插入数据
student = {
    'id': 2022110101,
    'name': 'Holy',
    'age': 20,
    'gender': 'male'
}
result = collection.insert_one(student)
print(result)

# 插入多条数据,以列表的形式传入
student1 = {
    'id': 2022110102,
    'name': 'Jack',
    'age': 22,
    'gender': 'male'
}
student2 = {
    'id': 2022110103,
    'name': 'Tom',
    'age': 10,
    'gender': 'male'
}
student3 = {
    'id': 2022110102,
    'name': 'Mike',
    'age': 22,
    'gender': 'male'
}
result = collection.insert_many([student1, student2, student3])
print(result)
print(result.inserted_ids)

# 查询
result = collection.find_one({'name': 'Tom'})
print(type(result))
print(result)
# 根据ObjectId查询,使用bson库里面的Objects
from bson.objectid import ObjectId

result = collection.find_one({'_id': ObjectId('63612746ba338fdea9246595')})
print(result)
# 查询多个结果使用find方法
results = collection.find({'age': {'$lt':20}})
print(results)
for res in results:
    print(res)
