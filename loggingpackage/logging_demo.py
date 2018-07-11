import logging

import loggingpackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug("DEBUG MESSAGE")
        self.log.info("INFO MESSAGE")
        self.log.error("ERROR MESSAGE")
        self.log.critical("CRITICAL MESSAGE")
        self.log.warning("WARNING MESSAGE")

    def method2(self):
        m2log = cl.customLogger(logging.INFO)
        m2log.debug("DEBUG MESSAGE")
        m2log.info("INFO MESSAGE")
        m2log.error("ERROR MESSAGE")
        m2log.critical("CRITICAL MESSAGE")
        m2log.warning("WARNING MESSAGE")

    def method3(self):
        m3log = cl.customLogger(logging.INFO)
        m3log.debug("DEBUG MESSAGE")
        m3log.info("INFO MESSAGE")
        m3log.error("ERROR MESSAGE")
        m3log.critical("CRITICAL MESSAGE")
        m3log.warning("WARNING MESSAGE")


demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()
