from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv

def get_link(element):
  elems = soup.select(element)
  return elems[0].get('href')

driver = webdriver.Chrome()
driver.get("http://naruto.wikia.com/wiki/List_of_Animated_Media")

html = driver.page_source
soup = BeautifulSoup(html, "lxml")



# FOR GETTING LIST

outputFile = open('list.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
x=2

while (1):
    try:
        a = get_link('#mw-content-text > table:nth-of-type(2) > tbody > tr:nth-of-type(%s) > td:nth-of-type(1) > a' % x)
        outputWriter.writerow([str(a)])
        print(x)
        x=x+1
    except Exception:
        outputFile.close()
        driver.quit()
        break
