from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl
import time

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _notification_link ="//iframe[@id='nvpush_popup_background_iframe']/following-sibling::div[@id='nvpush_cross']"
    _login_link = "Login"
    _email_field = "email"
    _password_field = "password"
    _login_button = ".//*[@id='logInForm']/input"
    _login_success = ".//*[@id='header']//span[text()='Hi jasbir']"
    _google_link = "//div[@id='tab-1-content']//div[@id='customBtnLogin']/span[text()='Google']"
    _email_fieldnew = "identifierId"
    _next_button = ".//*[@id='identifierNext']/content/span"
    _googlepassword_field = ".//*[@type='password']"
    _click_next = ".//*[@id='passwordNext']/content/span"
    _click_button =".//*[@id='passwordNext']/content"
    _cart_click = ".//*[@id='header']//span[@class='cart-text']"
    _profile_dropdown =".//*[@id='header']//span[contains(text(),'Hi')]"
    _logout_link =".//*[@id='header']//a[contains(text(),'Logout')]"

    def clickNotificationLink(self):
        if (self.isElementPresent(self._notification_link,locatorType="xpath")):
            self.elementClick(self._notification_link,locatorType="xpath")
        else:
            self.log.info("Notification link is already closed")

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field,locatorType="id")

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="xpath")

    def clickGooglelink(self,element):
        if (self.isElementPresent(self._google_link,locatorType="xpath") == True):
            self.elementClick(element,locatorType="xpath")
        else:
            print("Hello")
    def entergooglemail(self,email):
        self.sendKeys(email,self._email_fieldnew)

    def entergooglepassword(self,password):
        self.sendKeys(password,self._googlepassword_field,locatorType="xpath")

    def clicknext(self):
        self.elementClick(self._next_button,locatorType="xpath")

    def clicksend(self, locator, locatortype):
            self.elementClick(locator,locatortype)




    def login(self,username="",password=""):
        self.clickNotificationLink()
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()


    def loginGoogle(self,email,password):
        self.clickNotificationLink()
        self.clickLoginLink()
        element = self.getElement(self._google_link,locatorType="xpath")
        window_before = self.driver.current_window_handle
        self.moveToElementandClick(element)
        handles = self.driver.window_handles
        for handle in handles:
            if handle not in window_before:
                self.driver.switch_to.window(handle)
                self.entergooglemail(email)
                self.clicknext()
                self.entergooglepassword(password)
                self.clicksend(self._click_button,locatortype="xpath")
            self.driver.switch_to.window(window_before)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._login_success,locatorType="xpath")
        if self.isElementPresent(self._login_success, locatorType="xpath"):
            self.logout()
        else:
            print("Login Unsuccessful")
        return result

    def verifyLoginSuccessfulgoogle(self):
        resultnew = self.isElementPresent(self._login_success,locatorType="xpath")
        return resultnew

    def verifyLoginFailed(self):
        result = self.isElementPresent(".//p[contains(text(),'Email/Number or password is invalid')]",
                                       locatorType="xpath")
        self.clicksend(".//*[@id='closeBtnId']","xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()


    def visitCategoryPage(self,product,category):
        ele= self.getElement(product,locatorType="xpath")
        catele = self.getElement(category, locatorType="xpath")
        self.moveToElementandClick(ele)
        self.moveToElementandClick(catele)

    def removeCart(self):
        self.clicksend(self._cart_click,locatortype="xpath")

    def logout(self):
        ele = self.getElement(self._profile_dropdown,locatorType="xpath")
        logele = self.getElement(self._logout_link,locatorType="xpath")
        self.moveToElementandClick(ele)
        self.moveToElementandClick(logele)


