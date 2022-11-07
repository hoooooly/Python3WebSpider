import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('D:/Users/chromedriver.exe')

browser.get('https://www.taobao.com')
browser.get('https://www.baidu.com')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.close()
