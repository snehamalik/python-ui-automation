import pytest
from utilities.teststatus import TestStatus
from pages.home.login_page import LoginPage
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.subscription_page import SubscriptionPage
import time

@ddt
class subscriptionTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.su = SubscriptionPage(self.driver)


    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\sneha.malik\PycharmProjects\simpleframework\\subscription_data.csv"))
    @unpack
    def test_subscription(self,email):
        print(email)
        self.su.send_email(email)
        self.su.subscribed_user()
        time.sleep(2)
        self.su.refreshbrowser()




