from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class MouseHovering():
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


        # At first scrool the page to see the intended element
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)
        # Find the element of mouse hover
        element = driver.find_element(By.ID,"mousehover")
        # Find the Locator / option to click at the mouse hover
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            # for actions like mouse hovering we have to use selenium method Action Chains
            actions = ActionChains(driver) # here actions is the object we created from the class ActionChains
            # For every actions we have to run move to element method and perform the action
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH,itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on element")











run_test = MouseHovering()
run_test.test()