import requests

r = requests.get('https://www.baidu.com')
print(type(r.cookies), r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)
