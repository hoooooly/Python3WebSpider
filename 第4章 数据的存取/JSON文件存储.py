import json

str = '''
[{
    "name":"bob",
    "gender":"male",
    "birthday":"1992-10-19"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
'''

print(type(str))
data = json.loads(str)
print(data)
print(type(data))

