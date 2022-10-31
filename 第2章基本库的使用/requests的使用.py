import requests

r = requests.get('https://www.baidu.com')
print(type(r))  # <class 'requests.models.Response'>
print(r.status_code)  # 200
print(type(r.text))  # <class 'str'>
print(r.text[:100])  # <!DOCTYPE html>
# <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;chars
print(r.cookies)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

"""GET请求
"""

r = requests.get('https://www.httpbin.org/get')
print(r.text)
'''执行结果：
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-635d681f-5159eeed29f6b99237e959d4"
  }, 
  "origin": "45.78.49.194", 
  "url": "https://www.httpbin.org/get"
}
'''

"""params参数"""
data = {
    'name': 'germey',
    'age': 25
}

r = requests.get('https://www.httpbin.org/get', params=data)
print(r.text)
'''执行结果：
{
  "args": {
    "age": "25", 
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-635d692f-54b964f0791cb9cc3c740656"
  }, 
  "origin": "45.78.49.194", 
  "url": "https://www.httpbin.org/get?name=germey&age=25"
}
'''



