"""
Logging Levels: Levels means kinds of information we want
to write towards the console or file so that we can differentiate
between different kinds of actions performed by the application.
Here is some levels....
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging
logging.warning("warning message")
logging.info("infor message") # its not gonna print the info because
#by default the threshold is set to warning.so it will print only messages
# that are above warning level and that were warnig,error and critical.