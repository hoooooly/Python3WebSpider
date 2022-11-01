"""
pip install pyquery
"""

html = '''<div>
    <ul>
        <li class="li item-0"><a href="link1.html">first item</a></li>
        <li class="li item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>'''

from pyquery import PyQuery as pq

'''字符串初始化'''
doc = pq(html)
print(doc('li'))

'''url初始化'''
doc = pq('https://cuiqingcai.com')
print(doc('title'))
'''文件初始化'''
doc = pq(filename='test.html')
print(doc('title'))