from selenium import webdriver

class FindIdByName():
    def test(self):

        # At First We Have To Show The Path Where Is The Geckodriver Located
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        # Instantiate Firefox Browser Command
        driver = webdriver.Firefox(executable_path=driverlocation)
        driver.get("https://learn.letskodeit.com/p/practice")
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by Name")

ff = FindIdByName()
ff.test()