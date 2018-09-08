from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv, pyautogui, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('/home/akshat/Workspace/Naruto_Scrapping/Nimbus-Screenshot-&-Screen-Video-Recorder_v8.6.5.crx')
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1366, 768)

driver.get('https://en.wikipedia.org/wiki/Jabalpur')


time.sleep(10)
driver.quit()
