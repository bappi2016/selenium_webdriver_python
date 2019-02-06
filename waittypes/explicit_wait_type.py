from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utilities.handy_wrappers import HandyWrappers
import time
from traceback import print_stack

class ExplicitWaitType():

    def __init__(self,driver):
        self.driver = driver
        self.hw  = HandyWrappers(driver)

    # Default timeout is 10
    def waitForElement(self,locator_name,locatorType="id",
                       timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)

            print("Waiting for maximum::"+str(timeout)+
                  " :: seconds for element to be clickable")
            # Set explicit wait for element by webdriver wait
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable(byType, "stopFilter_stops-0"))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element


run_test = ExplicitWaitType()
run_test.waitForElement()

