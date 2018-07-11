from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import logging
import utilities.custom_logger as cl

class addressPage(LoginPage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _select_address="//a[contains(@href,'selectedAddressId')][text()='Select Address']"

    def clickFirstAddress(self):
        self.clicksend(self._select_address,locatortype="xpath")


