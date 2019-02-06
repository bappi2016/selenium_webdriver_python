from selenium import  webdriver
from selenium.webdriver.support.select import Select
import time

class WorkWithHiddenElement():
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

        # At first find the element  of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        # Now find the textbox state is it hide or show
        textBoxState = textBoxElement.is_displayed() #True if visible, false if hidden
        # Exception if not present in the DOM
        print ("Is the text visisble? " + str(textBoxState))

        #Click the Hide button
        driver.find_element_by_id("hide-textbox").click()
        time.sleep(2)

        #Again find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Is the text visisble? " + str(textBoxState))


        #click the show button
        driver.find_element_by_id("show-textbox").click()
        time.sleep(2)

        #Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print ("Is the text visisble? " + str(textBoxState))

        #close the browser
        driver.quit()

    def testExpedia(self):
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        # now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.expedia.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(10)

        driver.find_element_by_id("tab-flight-tab").click()
        drpdwnElement = driver.find_element_by_id("flight-age-select-1")
        print ("Is Element visible ? " + str(drpdwnElement.is_displayed()))










run_test = WorkWithHiddenElement()
run_test.test()
run_test.testExpedia()