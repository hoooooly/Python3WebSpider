import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(type(response))
'''
输出结果<class 'http.client.HTTPResponse'>
响应是HTTPResponse类型的对象，有read、readinto、getheader、getheaders、fileno等方法
以及msg、version、status、reason、debuglevel、closed等属性
'''
# print(response.read().decode('utf-8'))    # 输出网页源代码
print(response.status)  # 状态码
'''200'''
print(response.getheaders())  # 响应头
'''[('Connection', 'close'), ('Content-Length', '51106'), ('Server', 'nginx'),
 ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'DENY'),
  ('Via', '1.1 vegur, 1.1 varnish, 1.1 varnish'), ('Accept-Ranges', 'bytes'),
   ('Date', 'Sat, 29 Oct 2022 17:04:14 GMT'), ('Age', '1975'),
    ('X-Served-By', 'cache-iad-kiad7000025-IAD, cache-itm18844-ITM'), ('X-Cache', 'HIT, HIT'), 
    ('X-Cache-Hits', '459, 2'), ('X-Timer', 'S1667063055.850658,VS0,VE0'), ('Vary', 'Cookie'), 
    ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')]'''
print(response.getheader('Server'))  # 获取响应头中Server信息
'''nginx'''

