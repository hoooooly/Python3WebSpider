import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('D:/Users/chromedriver.exe')

browser.get('https://www.taobao.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.baidu.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])

browser.get('https://www.python.org/')

time.sleep(3)
browser.close()
