from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl
from pages.home.login_page import LoginPage


class SubscriptionPage(LoginPage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _subscription_page=".//*[@name='nl-home-widget-email']"
    _subscribe_button=".//*[@value='Subscribe']"
    _subscription_text=".//*[@id='root']/div/div[2]/div/section[9]/div/section/form/div/div/div/h3"


    def send_email(self,email):
        self.clickNotificationLink()
        self.sendKeys(email,self._subscription_page,locatorType="xpath")

    def subscribed_user(self):
        self.clicksend(self._subscribe_button,locatortype="xpath")

    def refreshbrowser(self):
        ele=self.getElement(self._subscription_text,locatorType="xpath")
        self.driver.get("https://www.healthkart.com")

