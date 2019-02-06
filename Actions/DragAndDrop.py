from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class DragAndDrop():
    def test(self):

        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable "driverlocation" which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # At first maximize the window
        driver.maximize_window()
        # Open The Provided URL with driver.get method
        baseURL = "http://www.jqueryui.com/droppable"
        driver.get(baseURL)
        # wait until the browser is fully loaded by implicitly_wait method
        driver.implicitly_wait(3)


        # At first switch to the iframe where is the drag and drop element located
        driver.switch_to.frame(0)

        fromElement = driver.find_element(By.ID,"draggable")
        toElement = driver.find_element(By.ID,"droppable")
        time.sleep(2)
        try:
            # for actions like mouse hovering we have to use selenium method Action Chains
            actions = ActionChains(driver) # here actions is the object we created from the class ActionChains
            # For every actions we have to run move to element method and perform the action
            # actions.drag_and_drop(fromElement,toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print("Drag and Drop Element Successfully")
            time.sleep(2)

        except:
            print("Drag And Drop failed on element")











run_test = DragAndDrop()
run_test.test()