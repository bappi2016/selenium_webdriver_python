from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class screenShots():
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

        driver.find_element(By.LINK_TEXT,"Login").click()
        driver.find_element(By.ID,"user_email").send_keys("abc@gmail.com")
        driver.find_element(By.ID,"user_password").send_keys("abc")
        driver.find_element(By.NAME,"commit").click()
        self.takeScreenshot(driver)

    def takeScreenshot(self,driver):
        """
        Takes screen shot of the current open web page with parameter driver and return it
        :param driver:
        :return:
        """
        genarate_a_fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/home/bappi/Documents/webdriver_screenshot"
        desired_screenshot = screenshotDirectory + genarate_a_fileName

        try:
            driver.save_screenshot(desired_screenshot)
            # driver.save_screenshot will take a screen shot and save it
            print("Screenshot saved to directory :: -> " + desired_screenshot)
        except NotADirectoryError:
            print("Not a directory issue")


run_test = screenShots()
run_test.test()