import pytest
from utilities.teststatus import TestStatus
from pages.home.order_placement_page import orderPlacementPage
from pages.home.login_page import LoginPage
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class orderPlacementCod(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.op = orderPlacementPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_orderPlacement(self):
        self.lp.login("9818152283","malik")
        self.op.orderplacecod()

