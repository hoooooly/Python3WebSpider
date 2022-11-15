import time

import requests
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.common.by import *

browser = webdriver.Chrome('D:/Users/chromedriver.exe')

BASE_URL = 'https://login2.scrape.center'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')

USERNAME = 'admin'
PASSWORD = 'admin'

browser.get(BASE_URL)
browser.find_element(by=By.CSS_SELECTOR, value='input[name="username"]').send_keys(USERNAME)
browser.find_element(by=By.CSS_SELECTOR, value='input[name="password"]').send_keys(PASSWORD)
browser.find_element(by=By.CSS_SELECTOR, value='input[type="submit"]').click()

time.sleep(5)

cookies = browser.get_cookies()
print(cookies)
browser.close()

# 将cookie 信息放入请求中
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])


response_index = session.get(INDEX_URL, )
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
