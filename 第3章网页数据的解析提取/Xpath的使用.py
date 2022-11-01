"""
XPath的使用
nodename    选取此节点的所有子节点
/   从当前节点直接选取子节点
//  从当前节点选取子孙节点
.   选取当前节点
..  选取当前节点的父节点
@   选取属性

安装
pip install lxml
"""
import logging

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
# print(result.decode('utf-8'))

"""所有节点"""
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])

"""子节点"""
result = html.xpath('//li/a')
print(result)

result = html.xpath('//li//a')
print(result)

"""父节点"""
print("-" * 50 + "父节点" + "-" * 50)
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
'''输出结果：
['item-1']
'''
# 通过parent::获取父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
'''输出结果：
['item-1']
'''

"""属性匹配
通过@进行属性匹配
"""
print("-" * 50 + "属性匹配" + "-" * 50)
result = html.xpath('//li[@class="item-0"]')
print(result)

"""文本获取"""
print("-" * 50 + "文本获取" + "-" * 50)
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

"""属性获取"""
print("-" * 50 + "属性获取" + "-" * 50)
result = html.xpath('//li/a/@href')
print(result)

"""属性多值匹配"""
print("-" * 50 + "属性多值匹配" + "-" * 50)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)