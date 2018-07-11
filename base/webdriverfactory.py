import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self,browser):

        self.browser = browser


    def getWebDriverInstance(self):
        baseURL = "https://www.healthkart.com"

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "firefox":
            # Set chrome driver
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)
        return driver

