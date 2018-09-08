from selenium import webdriver
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
try:
    driver.set_page_load_timeout(15)
    driver.get("http://www.engadget.com")
except TimeoutException as ex:
    isrunning = 0
    print("Exception has been thrown. " + str(ex))
    driver.close()
