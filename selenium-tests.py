from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options 
import os

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
username=os.environ.get("LOGIN_USERNAME")
password=os.environ.get("LOGIN_PASSWORD")
driver=webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
try:
    driver.get("http://localhost:8000") #cloudurl
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("submit").send_keys(Keys.ENTER)
except:
    print("Unit testing failed")
driver.close()
