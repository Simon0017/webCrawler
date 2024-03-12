# import webdriver 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

# create webdriver object 
driver = webdriver.Firefox() 

# get geeksforgeeks.org 
driver.get("https://simon0017.github.io/strapgenventure.io/") 
	
# get element 
element = driver.find_element(By.CLASS_NAME,'main-nav')

# create a actiopn chain object
action = ActionChains(driver)



# click element 
element.click() 

