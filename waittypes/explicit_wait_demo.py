from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from waittypes.explicit_wait_type import ExplicitWaitType

import time


class ExplicitWaitDemo():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driverlocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.crome.driver"] = driverlocation
        # Instantiate Crome Browser Command
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        # create an object variable wait with driver instance of ExplicitWaitType class
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)

        driver.find_element(By.ID,"tab-flight-tab").click()
        driver.find_element(By.ID,"flight-origin").send_keys("SFO")
        driver.find_element(By.ID,"flight-destination").send_keys("NYC")
        driver.find_element(By.ID,"flight-departing").send_keys("12/14/2016")
        returnDate = driver.find_element(By.ID,"flight-returning")
        returnDate.clear()
        returnDate.send_keys("12/26/2016")
        driver.find_element(By.ID,"search-button").click()
        # Now call the method of ExplicitWaitType class with the help of the object
        # wait which is the object of that class
        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()




run_test = ExplicitWaitDemo()
run_test.test()

