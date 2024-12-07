from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Chromedriver initialisation
driver = webdriver.Chrome('D:\Selenium Practices\chromedriver-win64\chromedriver.exe')

#Open the practice website
url = "https://qavalidation.com/demo-form/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

#Finding the elements
fullName = driver.find_element(By.NAME, "g4072-fullname")
email = driver.find_element(By.NAME, "g4072-email")
phone = driver.find_element(By.NAME, "g4072-phonenumber")
gender = driver.find_element(By.XPATH, "//select[@name='g4072-gender']/option[text()='Male']") #Selecting gender as Male
experience = driver.find_element(By.ID, "g4072-yearsofexperience-2")
skill1 = driver.find_element(By.ID, "g4072-skills-Functional testing")
skill2 = driver.find_element(By.ID, "g4072-skills-Automation testing")
skill3 = driver.find_element(By.ID, "g4072-skills-DB testing")
tools = driver.find_element(By.XPATH, "//select[@name='g4072-qatools']/option[text()='Selenium']") #Selecting tools as Selenium
comments = driver.find_element(By.NAME, "g4072-otherdetails")
submitButton = driver.find_element(By.XPATH, "//button[@type='submit']")

#Entering the details
fullName.send_keys("Venkatesan S K")
email.send_keys("venkatesan.sk221@gmail.com")
phone.send_keys("9876543210")
gender.click()
experience.click()
skill1.click()
skill2.click()
skill3.click()
tools.click()
comments.send_keys("Test")
submitButton.click() #Comment this line to check negative scenario
try:
    successMessage = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//h4[@id='contact-form-success-header']"))
    )
    print("Form submitted successfully!!!")
except:
    print("Something went wrong...")
finally:
    driver.quit() #Ends the program