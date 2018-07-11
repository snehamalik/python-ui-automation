import logging

class LoggerDemoConsole():
    def testLog(self):
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s -%(name)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        chandler.setFormatter(formatter)

        logger.addHandler(chandler)

        logger.debug("DEBUG MESSAGE")
        logger.info("INFO MESSAGE")
        logger.error("ERROR MESSAGE")
        logger.critical("CRITICAL MESSAGE")
        logger.warning("WARNING MESSAGE")

demo = LoggerDemoConsole()
demo.testLog()






