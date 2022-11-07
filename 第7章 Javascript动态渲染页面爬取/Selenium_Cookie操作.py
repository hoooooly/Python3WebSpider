import time

from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('D:/Users/chromedriver.exe')

browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())