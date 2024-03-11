import requests
from bs4 import BeautifulSoup

# making request GET
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code ie 200 for success
print(r)

# parsing the html 
soup = BeautifulSoup(r.content,'html.parser')
# print(soup.prettify())

s = soup.find('div',class_='entry-content')
content = s.find_all('p')
# print(content)

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options #to prevent the b rowser from closing itself

# for holding the resultant list
element_list = []

for page in range(1,3,1):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
    r_options = Options()
    r_options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=r_options)
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME,'title')
    price = driver.find_elements(By.CLASS_NAME,'price')
    description = driver.find_elements(By.CLASS_NAME,'description')
    rating = driver.find_elements(By.CLASS_NAME,'ratings')

    for i in range(len(title)):
        element_list.append([title[i].text,price[i].text,description[i].text,rating[i].text])
print(element_list)
driver.close()


