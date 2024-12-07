from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from prettytable import PrettyTable #For displaying as neatly formatted table in output
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website
url = "https://www.amazon.in/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

table = PrettyTable(["S.no", "Brand", "Price"])

#Searching in amazon
search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox'][@name='field-keywords']")
search.send_keys("Shirt")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(15)
#Getting all the details
collections = driver.find_elements(By.XPATH,"//div[@data-cy='asin-faceout-container']")

#Getting brand and price to print
for i in range(10):
    driver.implicitly_wait(15)
    brand = collections[i].find_elements(By.XPATH,"//span[@class='a-size-base-plus a-color-base']")[i]
    price = collections[i].find_elements(By.XPATH,"//span[@class='a-price-whole']")[i] 
    table.add_row([i+1, brand.text, price.text])

driver.quit()
print(table)