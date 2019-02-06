from selenium import  webdriver
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():
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



        # Find the drop down element
        dropdownelement =driver.find_element_by_id("carselect")
        #now select the element by Selenium provided method Select()
        select_element = Select(dropdownelement)
        #now work with the selected element
        select_element.select_by_value("benz")
        print ("Select Benz by value")
        time.sleep(2)


        select_element.deselect_by_visible_text("BMW")
        print ("Select BMW  by visible text")
        time.sleep(2)

        select_element.deselect_by_index("2")
        print ("Select Honda by index")
        time.sleep(2)

        print ("Select Benz by value")
        time.sleep(2)

















run_test = DropdownSelect()
run_test.test()