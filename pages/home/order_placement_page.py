import logging
import utilities.custom_logger as cl
from pages.home.address_page import addressPage
from pages.home.payment_page import paymentPage


class orderPlacementPage(addressPage, paymentPage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _product_visit = "//section[@class='hkheader-nav hidden-xs']//div[@id='dropDownbox1']/ul/li[2]"
    _category_clicked = ".//section[@class='hkheader-nav hidden-xs']//div[@id='dropDownbox1']//li[@class='menu-label shop-by-product more-catlinks']//ul//a[contains(text(),'Whey Proteins')]"
    _variant_clicked = ".//*[@id='variantResultView']//a/h2[contains(text(),'MuscleBlaze Whey')]"
    _buy_clicked = ".//*[@id='variant-page']//div[@class='buy-now-container']"
    _ptc_clicked = ".//*[@id='status']//a[contains(text(),'Proceed to checkout')]"

    def orderplacecod(self):
        self.visitCategoryPage(self._product_visit, self._category_clicked)
        self.clicksend(self._variant_clicked, locatortype="xpath")
        self.clicksend(self._buy_clicked, locatortype="xpath")
        self.clicksend(self._ptc_clicked, locatortype="xpath")
        self.clickFirstAddress()
        self.selectCod()
        self.placeOrder()