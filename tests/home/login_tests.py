import pytest
from utilities.teststatus import TestStatus
from pages.home.login_page import LoginPage
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class loginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        #not_link ='.//*[@id="nvpush_cross"]/svg'
        self.lp.login('9818152283','malik')
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1,"")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result2,"Login was not successful")


    @pytest.mark.run(order=1)
    @data(*getCSVData("C:\\Users\\sneha.malik\PycharmProjects\simpleframework\\test_data.csv"))
    #@data(("9818152283","abc"),("9899059627","malik"))
    @unpack
    def test_invalidLogin(self,mobilenumber,password):
        self.lp.login(mobilenumber,password)
        result = self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin",result,"Invalid password has been entered")


    # @pytest.mark.run(order=3)
    # def test_googleLogin(self):
    #     self.lp.loginGoogle("sneha.malik@brightlifecare.com","mapa@2580")
    #     result = self.lp.verifyLoginSuccessful()
    #     assert result == True
    #     self.ts.markFinal("test_googleLogin",result,"Invalid google login")
