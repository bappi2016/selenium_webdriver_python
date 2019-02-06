from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class autoComple():
    def test(self):

        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.southwest.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(3)

        # Send partial data to the text box to show the available option
        # first find the element of text field
        textField = driver.find_element_by_id("air-city-departure")
        textField.send_keys("New York")
        time.sleep(3)

        # Now the auto complete will show up and choose one of them
        itemToSelect = driver.find_element_by_xpath\
            ("//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        itemToSelect.click()

        #time.sleep(3)
        #driver.quit()


run_test = autoComple()
run_test.test()