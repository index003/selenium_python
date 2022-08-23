import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.quit()

