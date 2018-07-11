from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import selenium
from selenium.common.exceptions import *
from traceback import print_stack
import logging
import utilities.custom_logger as cl
import time

class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            time.sleep(3)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator " + locator + " locator type: "+locatorType)
        except:
            self.log.info("Element not found with locator " + locator + " locator type: "+locatorType)
        return element

    def getElements(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            time.sleep(2)
            element = self.driver.find_elements(locator,locatorType)
            self.log.info("Element Found with locator " + locator + " locator type: " + locatorType)
        except:
            self.log.info("Element not found with locator " + locator + " locator type: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on the element with locator: "+locator +" locator type: " + locatorType)
        except:
           self.log.info("Cannot click on the element with locator: "+locator +" locator type: " + locatorType)
           print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sending data on the element with locator: " + locator + " locator type: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locator type: " + locatorType)
            print_stack()

    def waitForelement(self, locator, locatorType="id",timeout =10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum ::" + str(timeout) + ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver,timeout=timeout, poll_frequency= pollFrequency,ignored_exceptions=
            [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web Page")
            print_stack()
        return element

    def isElementPresent(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False


    def moveToElementandClick(self,element):
        try:
            self.ele=element
            #element = self.getElement(locator,locatorType)
            self.log.info("element with value:" + str(self.ele) + " is found")
            hover=ActionChains(self.driver).move_to_element(self.ele).click().perform()
            self.log.info("move to element with id has been done")
            time.sleep(10)
            #actions.move_to_element(element).click().perform()
        except:
            self.log.info("Element with locator "+ str(self.ele) +" is not found")

    def verifyTitle(self):
        if "Buy" in self.getTitle():
            return True
        else:
            return False








