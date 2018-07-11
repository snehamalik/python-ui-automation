import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)
    def __init__(self,driver):
        super(TestStatus, self).__init__(driver)
        self.resultList=[]

    def setResult(self,result,resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("Pass")
                    self.log.error("### VERIFICATION SUCCESSFUL :: "+ resultMessage)
                else:
                    self.resultList.append("Fail")
                    self.log.error("### VERIFICATION FAILED :: " + resultMessage)
            else:
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)
        except:
            self.log.error("### EXCEPTION OCCURED !!!")

    def mark(self,result,resultMessage):
        self.setResult(result,resultMessage)


    def markFinal(self,testName,result,resultMessage):
        self.setResult(result,resultMessage)

        if "Fail" in self.resultList:
            self.log.error(testName +" ### TEST FAILED")
            self.resultList.clear()
            assert True==False

        else:
            self.log.info(testName + " ### TEST IS SUCCESSFUL")
            self.resultList.clear()
            assert True==True


