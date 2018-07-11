import logging



#logging.basicConfig(filename='test.log',level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning("This is a warning msg")
logging.info("This is a info msg")
logging.error("Error message")