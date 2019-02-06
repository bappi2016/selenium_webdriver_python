from selenium import webdriver
import os

# Create A Class For Crome Test
class RunCromeTests():
    def chrome_test(self):
        #At First We Have To Show The Path Where Is The Cromedriver Located
        driverlocation = "/usr/local/bin/chromedriver"
        os.environ["webdriver.crome.driver"] = driverlocation
        #Instantiate Crome Browser Command
        driver = webdriver.Chrome(driverlocation)
        #Open The Provider URL
        driver.get("http://www.letskodeit.com")

#Now Create An Object To Run The Class
ff = RunCromeTests()
#Now Call The Method To Execute
ff.chrome_test()


