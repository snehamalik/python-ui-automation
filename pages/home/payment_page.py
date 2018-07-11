from pages.home.login_page import LoginPage
import logging
import utilities.custom_logger as cl

class paymentPage(LoginPage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    _cod_text=".//*[@id='nav']/li[contains(text(),'CASH ON DELIVERY')]"
    _cod_place_order=".//*[@id='tab10']//input[@name='makePayment']"

    def selectCod(self):
        self.clicksend(self._cod_text,locatortype="xpath")

    def placeOrder(self):
        self.clicksend(self._cod_place_order,locatortype="xpath")



