from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonAndCheckBox():
    def test(self):

        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(10)


        #find the element of radio button
        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        #now click the button
        bmwRadioBtn.click()

        #wait 2 seconds with sleep method
        time.sleep(2)

        #find another web element by id
        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        #find element with checkboxes
        time.sleep(2)
        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()

        # find element with checkboxes
        time.sleep(2)
        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        #now check if the selected item works accordingly

        print("BMW radio button is selected ? " + str(bmwRadioBtn.is_selected()))
        print("Benz radio button is selected ? " + str(benzRadioBtn.is_selected()))
        print("BMW CheckBox is selected ? " + str(bmwCheckbox.is_selected()))
        print("Benz checkbox is selected ? " + str(benzCheckbox.is_selected()))













run_test = RadioButtonAndCheckBox()
run_test.test()