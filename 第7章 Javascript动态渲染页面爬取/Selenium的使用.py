from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome('D:/Users/chromedriver')

try:
    browser.get('https://www.baidu.com')
    input_ = browser.find_element(by=By.ID, value='kw')
    input_.send_keys('Python')
    input_.send_keys(Keys.ENTER)
    wait_ = WebDriverWait(browser, 10)
    wait_.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
