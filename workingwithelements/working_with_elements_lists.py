from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():
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


        #find all the radio buttons lists by find_elements
        radioButtonList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars') ]"
        )
        #find the size of the list by len()
        size = len(radioButtonList)
        print ("size of the list: "+ str(size))

        #run a loop for check all the button is select or not
        for radioButton in radioButtonList:
            isSelected = radioButton.is_selected()
            #if not selected any button then select
            if not isSelected:
                radioButton.click()
                time.sleep(2)













run_test = WorkingWithElementsList()
run_test.test()