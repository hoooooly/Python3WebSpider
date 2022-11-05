import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import *

browser = webdriver.Chrome('D:/Users/chromedriver')

browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

browser.switch_to.frame('iframeResult')
source = browser.find_element(by=By.CSS_SELECTOR, value='#draggable')
target = browser.find_element(by=By.CSS_SELECTOR, value='#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

time.sleep(10)
browser.close()
