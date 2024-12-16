from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable #For displaying as neatly formatted table in output
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website
url = "https://www.tutorialspoint.com/selenium/practice/webtables.php"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

#Retriving table headers and data
tableHeaders = driver.find_elements(By.XPATH, "//thead/tr")
tableData = driver.find_elements(By.XPATH, "//tbody/tr")
headerList = [] #Table header

#Getting table headers as list
for header in tableHeaders:
    firstName = header.find_elements(By.TAG_NAME, 'th')[0]
    age = header.find_elements(By.TAG_NAME, 'th')[2]
    salary = header.find_elements(By.TAG_NAME, 'th')[4]
    headerList.extend([firstName.text, age.text, salary.text])

table = PrettyTable(headerList) #Initialising table

#Getting tablr data as list and appending to table
for data in tableData:
    firstName = data.find_elements(By.TAG_NAME, 'td')[0]
    age = data.find_elements(By.TAG_NAME, 'td')[2]
    salary = data.find_elements(By.TAG_NAME, 'td')[4]
    table.add_row([firstName.text, age.text, salary.text])

time.sleep(5)
driver.quit()#Ends the driver

print(table)#Prints the webtable