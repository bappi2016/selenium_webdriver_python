from selenium import webdriver
import  os

class FindByCSSSelector():
    def findbycssselector(self):
        driverlocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.get("https://learn.letskodeit.com/p/practice")
        #elementByCSSSelector = driver.find_element_by_css_selector("carselect")
        elementByClassName = driver.find_element_by_class_name("right-align")
        #elementByXPath = driver.find_element_by_xpath("1")

        #if elementByCSSSelector is not None:
            #print("We found an element by CSS Selector")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        #if elementByXPath is not None:
            #print("We found an element by XPath")

crome_test = FindByCSSSelector()
crome_test.findbycssselector()