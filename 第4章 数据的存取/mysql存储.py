import logging
import pymysql

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()  # 获取MySQL操作游标
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()  # 取得数据
logging.info('Database Version:%s', data)

# 创建数据库，执行一次就可以
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4')

# 创建表
sql = "CREATE TABLE IF NOT EXISTS STUDENTS " \
      "(ID VARCHAR(255) NOT NULL, " \
      "NAME VARCHAR(255) NOT NULL, " \
      "AGE INT NOT NULL, PRIMARY KEY (ID))"
cursor.execute(sql)

# 数据是一个字典
data = {
    'id': '20220302',
    'name': 'Tim',
    'age': 28
}

table_name = 'students'
keys = ','.join(data.keys())
values_format = ','.join(['%s'] * len(data))  # 构造占位符
sql = 'INSERT INTO {table}({keys}) VALUES ({values_format})'.format(table=table_name, keys=keys,
                                                                    values_format=values_format)

# 插入数据
try:
    cursor.execute(sql, tuple(data.values()))
    db.commit()  # 执行commit方法实现数据插入
    logging.info("数据插入成功")
except Exception as e:
    logging.debug(f"数据插入错误：{e}，执行回滚操作")
    db.rollback()  # 执行失败，回滚操作

# 更新数据
sql = 'UPDATE STUDENTS SET AGE = %s WHERE NAME = %s'
try:
    cursor.execute(sql, (18, 'Tom'))
    db.commit()  # 执行commit方法实现数据插入
    logging.info(f'数据更新成功: {sql.format("18", "Tom")}')
except Exception as e:
    logging.debug(e)
    db.rollback()  # 执行失败，回滚操作

# 删除数据
table_name = 'students'
condition = 'age > 29'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table_name, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 查询数据
sql = 'SELECT * FROM STUDENTS WHERE AGE >= 10'

try:
    cursor.execute(sql)
    logging.info(f'Count:{cursor.rowcount}')
    # one = cursor.fetchone()
    # logging.info(f'One:{one}')
    # results = cursor.fetchall()
    # logging.info(f'Results:{results}')
    # logging.info(f'Type Results:{type(results)}')
    # for row in results:
    #     logging.info(row)
    row = cursor.fetchone()
    while row:
        logging.info(f'Row:{row}')
        row = cursor.fetchone()

except Exception as e:
    logging.warning(f'Error:{e}')
db.close()
