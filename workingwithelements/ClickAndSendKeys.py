from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # Open The Provided URL with driver.get method
        baseURL = "http://www.letskodeit.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(10)


        # At first maximize the window
        driver.maximize_window()

        #find the web element of sign in  by XPATH
        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        #now click that link
        loginLink.click()

        #find the element of user email field
        emailField = driver.find_element(By.ID,"user_email")
        #type something in that field by send keys
        emailField.send_keys("test")

        #find the web element for password field
        passwordField = driver.find_element(By.ID,"user_password")
        passwordField.send_keys("test")

        #wait three seconds
        time.sleep(3)

        #now clear the emial field
        emailField.clear()

        # wait three seconds
        time.sleep(3)

        #test with another values
        emailField.send_keys("test")

run_test = ClickAndSendKeys()
run_test.test()