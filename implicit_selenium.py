# import webdriver 
from selenium import webdriver
from selenium.webdriver.common.by import By 

# create webdriver object 
driver = webdriver.Firefox() 
	
# set implicit wait time 
driver.implicitly_wait(10) # seconds 

# get geeksforgeeks.org 
driver.get("https://simon0017.github.io/strapgenventure.io/") 
	
# get element after 10 seconds 
element = driver.find_element(By.LINK_TEXT,'Contact Support')

# click element 
element.click() 

