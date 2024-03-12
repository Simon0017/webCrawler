# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.ID, "gsce-search-input")
 
# send keys
element.send_keys("Arrays")
