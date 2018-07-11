import logging
import logging.config

class LoggerDemoConf():
    def testLog(self):

       logging.config.fileConfig('logging.conf')
       logger = logging.getLogger(LoggerDemoConf.__name__)

       logger.debug("DEBUG MESSAGE")
       logger.info("INFO MESSAGE")
       logger.error("ERROR MESSAGE")
       logger.critical("CRITICAL MESSAGE")
       logger.warning("WARNING MESSAGE")

demo = LoggerDemoConf()
demo.testLog()