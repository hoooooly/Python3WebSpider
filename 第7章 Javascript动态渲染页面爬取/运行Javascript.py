import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome('D:/Users/chromedriver')

browser.get('https://www.zhihu.com/explore')

browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

browser.execute_script('alert("To Bottom")')




