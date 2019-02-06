import logging

# basicConfig is the method provided by logging model which we can
#use to provide the cofiguration the we want or the logs to follow
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p',
filename = "test.log",level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")