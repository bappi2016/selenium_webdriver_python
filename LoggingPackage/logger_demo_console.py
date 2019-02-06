import logging
class LoggerDemoConsole():
    def testLog(self):
        # create logger
        # At first create an object called logger with sample log as an arguments
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        # Now set the level of the logger as info, which not gonna print the
        # the debug statements but everything else
        logger.setLevel(logging.INFO)
        # logger will looks at the messages and create a log records object
        # from the message string and then pass it to the handler

        # create console handler and set level to info
        # handler is FINAL THING THAT IS responsible for the output of the messages
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)# any level below it , handler will ignore them
        # StreamHandler gonna bring the console and output the messages


        # create formatter
        formatter = logging.Formatter('%(asctime)s: -%(name)s -%(levelname)s: %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S %p')

        # add or set formatter to console handler ->ch
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)


        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()



