from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class AirbnbExercise():
    def test(self):

        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.airbnb.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(10)


        # At first find the search Box
        searchBox = driver.find_element(
            By.XPATH,"//div[@id='searchbar']//input[@name='location']")
        searchBox.send_keys("Hawaii")


        #find the element of check in
        check_in = driver.find_element_by_id("startDate")
        check_in.send_keys("12/20/2016")

        # find the element of check out
        checkout = driver.find_element_by_id("endDate")
        checkout.send_keys("12/31/2016")

        # Now find the drop down element
        dropdownelement = driver.find_element(By.NAME,"guests")
        # Now select the element by SELENIUM provided method Select()
        select_element = Select(dropdownelement)
        # Now find the element of drop down list
        select_element.select_by_visible_text("2 Guests")

        print ("select one dropdown element by its value")
        time.sleep(2)

        search_button = driver.find_element(
            By.XPATH,"div[@id='searchbar']//span[text()='Search']")
        search_button.click()



run_test = AirbnbExercise()
run_test.test()