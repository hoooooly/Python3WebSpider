import time

from selenium import webdriver
from selenium.webdriver.common.by import *

browser = webdriver.Chrome('D:/Users/chromedriver')

browser.get('https://www.taobao.com')

input = browser.find_element(by=By.ID, value='q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser.find_element(by=By.CLASS_NAME, value='btn-search')
button.click()
time.sleep(5)

browser.close()
