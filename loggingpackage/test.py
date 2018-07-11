import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



class ActionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Actions(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.healthkart.com')

        print(driver.title)

        element1 = driver.find_element_by_link_text("Login")
        time.sleep(10)
        element2 = driver.find_element_by_xpath("//div[@id='tab-1-content']//div[@id='customBtnLogin']/span[text()='Google']")
        driver.find_element_by_xpath("//iframe[@id='nvpush_popup_background_iframe']/following-sibling::div[@id='nvpush_cross']").click()
        window_before = driver.current_window_handle
        element1.click()
        hoverover = ActionChains(driver).move_to_element(element2).click().perform()
        time.sleep(10)
        handles = driver.window_handles
        for handle in handles:
            if handle not in window_before:
                driver.switch_to.window(handle)
                driver.find_element_by_id("identifierId").send_keys("sneha.malik@brightlifecare.com")
                driver.close()
        driver.switch_to.window(window_before)




        print(driver.title)

        driver.back()

    def tearDown(self):
        self.driver.close()


