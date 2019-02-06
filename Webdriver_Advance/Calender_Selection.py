from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class CalendarSelection():
    def test(self):
        # for firefox at first we have to show the path where is the Geckodriver located
        # we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        # now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.expedia.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH,
                        "//section[@class='cal-month'][position()=1]//a[text()='31']")
        # Click the date
        dateToSelect.click()

        time.sleep(3)

    def test2(self):
        # for firefox at first we have to show the path where is the Geckodriver located
        # we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        # now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.expedia.com"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(3)
        # Click flights tab
        driver.find_element_by_id("tab-flight-tab").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing")
        # Click departing field
        departingField.click()
        calMonth = driver.find_element(By.XPATH , "//section[@class='cal-month'][position()=1]")
        allValidDates = calMonth.find_element(By.TAG_NAME,"a")
        for date in allValidDates:
            if date.text == "31":
                date.click()
                break






run_test = CalendarSelection()
run_test.test()
run_test.test2()

