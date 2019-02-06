from selenium import webdriver

# Create A Class For FF Test
class RunFFTests():
    def ff_test(self):
        #At First We Have To Show The Path Where Is The Geckodriver Located
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #Instantiate Firefox Browser Command
        driver = webdriver.Firefox(executable_path=driverlocation)
        #Open The Provider URL
        driver.get("http://www.letskodeit.com")

#Now Create An Object To Run The Class
ff = RunFFTests()
#Now Call The Method To Execute
ff.ff_test()


