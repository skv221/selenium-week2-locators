from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website
url = "https://demo.openmrs.org/openmrs/login.htm"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5) #wait till all web elements loaded

className = driver.find_element(By.CLASS_NAME, "w-auto") #Locate element by class name
id = driver.find_element(By.ID, "Inpatient Ward") #Locate element by id
name = driver.find_element(By.NAME, "username") #Locate element by name
name.send_keys("ThisIsUsername") #Send some values to field to fetch
time.sleep(3) # wait to check if the field is populated
xpath = driver.find_element(By.XPATH, "//li[@id='Isolation Ward']") #Locate element by Xpath
selector = driver.find_element(By.CSS_SELECTOR, "a#cantLogin") #Locate element by css selectors

#prints the texts of the web elements
print(className.text)
print(id.text)
print(name.get_attribute('value'))
print(xpath.text)
print(selector.text)

driver.quit() #ends the program
