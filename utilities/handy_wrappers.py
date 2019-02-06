from selenium.webdriver.common.by import By
import selenium

class HandyWrappers():
    # Here we use the init method because we we will be needed
    # the driver instance (by passing arguments) to perform action, and we will be using
    # the object of this class, to use the method from this class
    # inside the classes, where we using it,so we need to pass arguments to that class
    # in order to initialize it.And here we need the driver instance
    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):# locatorType = ID,XPATH,etc...
        locatorType = locatorType.lower() # for avoid misspelling at first we convert it to lower
        if locatorType == "id": # Then we return the actual By.locator
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "tagname":
            return By.TAG_NAME
        else:
            print("Locator type does not support")
        return False
    # locator_name is the name which is in the html page as class name or id name
    def getElement(self,locator_name,locatorType = "id"):#positional or optional arguments as id
        # At first initialize element as none
        element = None
        try:
            locatorType = locatorType.lower()
            #byType variable will provide the locator type like id, xpath,class
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator_name)
            print("Element Found")
        except:
            print("Element Not Found")
        return element

    def isElementPresent(self,locator_name,byType):
        try:
            element = self.driver.find_element(byType, locator_name)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not Found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self,locator_name,byType):
        try:
            elementList = self.driver.find_element(byType, locator_name)
            if len(elementList) > 0 :
                print("Element Found")
                return True
            else:
                print("Element not Found")
                return False
        except:
            print("Element not found")
            return False



