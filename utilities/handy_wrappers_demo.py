from selenium import webdriver
import os
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():
    # Here we didn't need any init method because we didn't need
    # anything from outside, the test method take care everything
    def test(self):
        baseUrl = "http://letskodeit.teachable.com/pages/practice"
        driverlocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.crome.driver"] = driverlocation
        # Instantiate Crome Browser Command
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Now create an object hw which is the instance of the
        # HandyWrappers class

        hw = HandyWrappers(driver)

        textField = hw.getElement("name")
        textField.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']",locatorType="xpath")
        textField2.clear()

run_test = UsingWrappers()
run_test.test()
        
