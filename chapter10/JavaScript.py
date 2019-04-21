# Selenium
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome(r'M:\library\chromedriver\chromedriver.exe')
driver.get("http://120.79.60.89")
time.sleep(2)
print(driver.find_element_by_tag_name('div').text)

pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj)
driver.close()
