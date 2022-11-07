from selenium import webdriver
from selenium.webdriver.common.by import *
browser = webdriver.Chrome('D:/Users/chromedriver')

url = 'https://www.cnblogs.com/holychan/'

browser.get(url)

# 获取属性
title = browser.find_element(by=By.ID, value='Header1_HeaderTitle')

print(title)
print(title.get_attribute('href'))

# 获取节点文本信息
print(title.text)
# 获取节点ID
print(title.id)
# 获取节点相对位置
print(title.location)
# 获取标签名
print(title.tag_name)
# 获取节点的大小
print(title.size)
