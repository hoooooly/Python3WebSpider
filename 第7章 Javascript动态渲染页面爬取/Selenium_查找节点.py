from selenium import webdriver
from selenium.webdriver.common.by import *

browser = webdriver.Chrome('D:/Users/chromedriver')

browser.get('https://www.taobao.com')

input_first = browser.find_element(by=By.ID, value='q')
input_second = browser.find_element(by=By.CSS_SELECTOR, value='#q')
input_third = browser.find_element(by=By.XPATH, value='//*[@id="q"]')

# 查找多个节点
lis = browser.find_elements(by=By.CSS_SELECTOR, value='.service-bd li')

print(input_first)
print(input_second)
print(input_third)

print(lis)

browser.close()
