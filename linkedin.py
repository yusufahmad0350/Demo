from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Yusuf\\AppData\\Local\\Google\\Chrome\\NewProfile')

service = Service('./chromedriver')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.linkedin.com/in/yusufahmad786/')
print(driver.title)

input("Press enter to close the browser...")
driver.close()