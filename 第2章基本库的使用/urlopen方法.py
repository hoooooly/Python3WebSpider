import socket
import urllib.request
import urllib.parse
import urllib.error

"""data参数:
data参数是可选的，添加该参数时需要使用bytes方法将参数转成字节流编码格式，即bytes类型
如果传递了这个参数，那么请求就不是GET，而是POST
"""

data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
'''输出结果：
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "germey"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "www.httpbin.org", 
    "User-Agent": "Python-urllib/3.10", 
    "X-Amzn-Trace-Id": "Root=1-635d5f85-47afa909070c1c9746870553"
  }, 
  "json": null, 
  "origin": "45.78.49.194", 
  "url": "https://www.httpbin.org/post"
}
'''

"""timeout参数：
设置超时时间，单位为秒
可以通过设置超时时间，实现当一个网页长时间未响应时，就跳过对它的爬取
"""

# response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1) # 抛异常
# print(response.read())

try:
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
        '''输出结果：
            TIME OUT
        '''

