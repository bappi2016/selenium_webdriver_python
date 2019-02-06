from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat():
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

       # At first go to the  login option and click to the form to see the available courses
        driver.find_element(By.LINK_TEXT,"Login").click()
        # Now find the email field to the form
        emailField = driver.find_element(By.ID,"user_email")
        # Now type a email address
        emailField.send_keys("test@email.com")
        # Find the password field
        passwordField = driver.find_element(By.ID,"user_password")
        # Now type password
        passwordField.send_keys("abcabc")
        # Now click the commit button to continue
        driver.find_element(By.NAME,"commit").click()

        # Now search for available courses
        #  At first find the search box
        searchBox = driver.find_element(By.ID,"search-courses")
        searchBox.send_keys("JavaScript")

        #now select courses
        course = "//div[contains(@class,'course-listing-title')and contains(text(),'{0}')]"
        courseLocator = course.format("JavaScript for beginners")
        courseElement = driver.find_element(By.XPATH,courseLocator)
        courseElement.click()






run_test = DynamicXpathFormat()
run_test.test()