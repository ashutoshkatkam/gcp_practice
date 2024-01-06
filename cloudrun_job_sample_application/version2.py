# This is the version 2 code

import os
from google.cloud import logging
import argparse

# Instantiates a client
logging_client = logging.Client()

# The name of the log to write to
log_name = "myapp2-logs"
# Selects the log to write to
logger = logging_client.logger(log_name)

parser = argparse.ArgumentParser(description="Read and print the file name")
parser.add_argument("filename", help="The name of the file to read.")
args = parser.parse_args()

# Display the file name passed to the code
logger.info("Passed filename is "+ args.filename)

# The data to log
text = "log from version_2"

# Writes the log entry
logger.info(text)

# Reading the passed environemnt variable of the container.
env_2 = os.environ.get('ENV_2')

# Logging the environment variable of the container.
logger.info("Environment variable passed for ENV_2 is" + env_2)

