# This is the version 2 code

import os
import logging
import sys

logging.basicConfig(level=logging.INFO)


logging.info("Version 2 application started")

# Display the file name passed to the code
logging.info("Passed filename is "+ sys.argv[1])


# Reading the passed environemnt variable of the container.
env = os.environ.get('ENV')

# Logging the environment variable of the container.
logging.info("Environment variable passed for ENV is " + env)