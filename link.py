

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui,time,sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import os
import pandas as pd
""" Create a csv file with any column name, then add any company you want to target """



#Set your location of your csv input file
os.chdir(r'D:\Insta folders')
#Name the csv file as linkedin 
df= pd.read_csv('linkedin.csv')
 
pages= [i for i in range(1,20)]   
 
driver = webdriver.Firefox() 
 
 #Define the bots
driver.get('https://www.linkedin.com/')
driver.maximize_window()
time.sleep(3)

try:
    driver.find_element_by_id('session_key').send_keys('yusufahmad350@gmail.com')
except:
    driver.find_element_by_id('email-or-phone').send_keys('yusufahmad350@gmail.com')
    
time.sleep(3)
try:
    driver.find_element_by_id('session_password').send_keys('Yasmin@786')
except:
    driver.find_element_by_id('password').send_keys('Yasmin@786')
    
time.sleep(3) 
 
try:
    driver.find_element_by_id('session_password').send_keys(Keys.ENTER)
except:
    driver.find_element_by_id('password').send_keys(Keys.ENTER)
time.sleep(10)

print('yes')
print(df.values)
#LIST OF COMPANIES TO CLICK TO
for i in df.values:
    print(i)
    time.sleep(4)
    driver.find_element_by_xpath("//input[@class='search-global-typeahead__input'] ").send_keys(i)
    time.sleep(4)
    driver.find_element_by_xpath("//input[@class='search-global-typeahead__input']  ").send_keys(Keys.DOWN)

    time.sleep(4)   
    driver.find_element_by_xpath("//input[@class='search-global-typeahead__input'] ").send_keys(Keys.ENTER)
    time.sleep(4)
    see_allresults= driver.find_element_by_xpath("//a[@aria-label= 'See all people results']") 
    #click on all people search
    see_allresults.click()
    time.sleep(4)
    #CONNECT WITH PEOPLE
    try:
        Con= driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
         
    except:
        for i in range(10):
            driver.send_keys(Keys.DOWN)
            time.sleep(2)            
        Con= driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
    #print(Con)  
    print("connect")  
    
     
    currenturl= str(driver.current_url) + '&page='
    print(currenturl)
    for j in Con:
        if j.text == 'Connect':
            j.click()
            time.sleep(4)
            try:
                #sends= driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
                #sends.click()
                print('Clicked COnnect and entered Try')
                driver.find_element_by_xpath("//span[@class='artdeco-button__text' and text()= 'Send']").click()
                time.sleep(4)
            except:
                print('pop up')
                driver.find_element_by_xpath("//button[@class='artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view']").click()
                print('pressed Esc')
                continue         
            time.sleep(2)
    for pg in pages:
        driver.get(currenturl+ str(pg))
        #
        time.sleep(5)
        Con= driver.find_elements_by_xpath("//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']")
    
        #print(Con)  
        print("connect")
        for j in Con:
            if j.text == 'Connect':
                j.click()
                time.sleep(3)
                try:
                    #sends= driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
                    #sends.click()
                    print('Clicked COnnect and entered Try')
                    driver.find_element_by_xpath("//span[@class='artdeco-button__text' and text()= 'Send']").click()
                    time.sleep(4)
                except:
                    print('pop up')
                    driver.find_element_by_xpath("//button[@class='artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view']").click()
                    print('pressed Esc')
                    continue
                
                time.sleep(7)
        
    time.sleep(4)
    #CLEARING AND REPEATING OTHER COMPANY
    driver.find_element_by_xpath("//input[@class='search-global-typeahead__input']").clear()
    time.sleep(6)
    
 
