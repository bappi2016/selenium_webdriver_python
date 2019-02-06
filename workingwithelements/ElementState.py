from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

class ElementState():
    def test(self):

        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.google.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(10)

        #find the element by its id
        e1 = driver.find_element_by_id("gs_htif0")
        # now check that element is enable or disable by boolean method is_enabled
        e1State = e1.is_enabled() #True for enabled and False for disabled
        print("E1 is Enabled? - " + str(e1State))
        e1.send_keys("python language")

        # find the element by its id
        e2 = driver.find_element_by_id("gs_htif0")
        # now check that element is enable or disable by boolean method is_enabled
        e2State = e2.is_enabled()  # True for enabled and False for disabled
        print("E2 is Enabled? - " + str(e2State))








run_test = ElementState()
run_test.test()