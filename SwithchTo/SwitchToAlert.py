from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class SwitchToAlert():
    def test(self):

        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.letskodeit.teachable.com/p/practice.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(3)


        # At first find the text box field and then type your name
        driver.find_element(By.ID,"name").send_keys("Bappy")
        # Then find the alert button and  click the Alert Button
        driver.find_element(By.ID,"alertbtn").click()
        time.sleep(2)
        # Now switch to javascript alert popup window
        alert1 = driver.switch_to.alert
        # And then confirm it by clicking ok
        alert1.accept()
        time.sleep(2)

        # At first find the text box field and then type your name
        driver.find_element(By.ID, "name").send_keys("Bappy")
        # Then find the confirm button and  click the confirm Button
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        # Now switch to javascript alert popup window
        alert2 = driver.switch_to.alert
        # And then cancel it by clicking cancel
        alert2.dismiss()
        time.sleep(2)










run_test = SwitchToAlert()
run_test.test()