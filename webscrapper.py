import time
from selenium import webdriver

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

#get username, password and amount from terminal
userName = input("Username: ")
passWord = input("Password: ")
amountUSD = input("How much to pay: ")
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# go to payment url
driver.get("https://gogopher.appfolio.com/connect/users/sign_in")


#make objects for each element Selenium has to manipulate
username = driver.find_element_by_id("user_email")
password = driver.find_element_by_id("user_password")
button = driver.find_element_by_name("commit")

# fill fields with user and password data
username.send_keys(userName)
password.send_keys(passWord)
#hit continue button
button.click()
driver.implicitly_wait(10)

#Program continues to set button object to the correct elements for each page until next form
button = driver.find_element_by_class_name("js-pay-now-button")
button.click()
driver.implicitly_wait(10)

button = driver.find_element_by_name("ach")
button.click()
driver.implicitly_wait(10)

button = driver.find_element_by_name("commit")
button.click()

driver.implicitly_wait(10)
amountForm = driver.find_element_by_id("payment_amount")
amountForm.clear()
amountForm.send_keys(amountUSD)
driver.implicitly_wait(10)

button = driver.find_element_by_name("commit")
button.click()

answer = input("Are you sure you want to make payment of " + str(amountUSD) + " dollars? (y/n)")
if answer == "y":
    button = driver.find_element_by_name("commit")
    button.click()

time.sleep(3)
driver.quit()


