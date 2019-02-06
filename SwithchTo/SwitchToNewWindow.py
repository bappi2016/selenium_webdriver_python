from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class SwitchToNewWindow():
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

        # At first find parent handle which is Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Then find open window button and then click it
        driver.find_element(By.ID,"openwindow").click()

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to new window and search course
        for handle in handles:
            print("Handle" +handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to new window:" +handle)
                searchBox = driver.find_element(By.ID,"search-courses")
                searchBox.send_keys("python")
                time.sleep(3)
                driver.close()
                break

        # Switch back to the parent dandle
        driver.switch_to.window(parentHandle)




run_test = SwitchToNewWindow()
run_test.test()