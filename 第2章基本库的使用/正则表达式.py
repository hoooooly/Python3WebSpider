import re

content = 'Hello 123 4678 World_This is a Regex Demo'
# print(len(content))
# res = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(res)
# print(res.group())
# print(res.span())
#
# res = re.match('^Hello\s(\d+)\sWorld', content)
# print(res)
# print(res.group())
# print(res.span())

# 通用匹配
res = re.match('^Hello.*Demo$', content)
print(res)
print(res.group())
print(res.span())

# 非贪婪匹配
res = re.match('^He.*?(\d+\s\d+).*Demo$', content)
print(res)
print(res.group(1))
print(res.span())

# 修饰符
# re.I 忽略大小写
# re.S 匹配包含换行符在内的所有字符

