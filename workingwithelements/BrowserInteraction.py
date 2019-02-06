from selenium import  webdriver

class BrowserInteraction():
    def test(self):
        #for firefox at first we have to show the path where is the Geckodriver located
        #we set a variable driverlocation which will store the driver path
        driverlocation = "/usr/local/bin/gecko_driver/geckodriver"
        #now instantiate the firefox browser with the parameter of driver location
        driver = webdriver.Firefox(executable_path=driverlocation)
        # Open The Provider URL with driver.get method
        driver.get("http://www.letskodeit.com")


        # Window maximizing
        driver.maximize_window()

        #Open The URL


        #Get Title
        title = driver.title
        print("The title of the web page is "+title)

        #get current URL
        current_URL = driver.current_url
        print("Current URL of the web page is " +current_URL)



        #Browser refresh
        driver.refresh()
        print("Browser refresh for 1st time")

        #Go to previouse page
        driver.back()
        current_URL = driver.current_url
        print("Current URL of the web page is " + current_URL)
        print("Go one step back in browser history")


        #Go to next page
        driver.forward()
        current_URL = driver.current_url
        print("Current URL of the web page is " + current_URL)
        print("Go one step forward in browser history")

        # open another URL
        driver.get("http://www.facebook.com")
        current_URL = driver.current_url
        print("Current URL of the web page is " + current_URL)

        #Get page source


        #Browser Close/Quit










    #now create an object runtest to run the class BrowserInteraction()
runtest = BrowserInteraction()
#now call the method test to execute the code
runtest.test()