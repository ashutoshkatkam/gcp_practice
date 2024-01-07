# This is the version 1 code

import os
from google.cloud import logging
import argparse

# Instantiates a client
client = logging.Client(project="my-project")
logger = client.logger(name="my_app1_logs")

logger.log("Version 1 application started",severity="INFO")

parser = argparse.ArgumentParser(description="Read and print the file name")
parser.add_argument("filename", help="The name of the file to read.")
args = parser.parse_args()

# Display the file name passed to the code
logger.log("Passed filename is "+ args.filename,severity="INFO")


# Reading the passed environemnt variable of the container.
env = os.environ.get('ENV_1')

# Logging the environment variable of the container.
logger.log("Environment variable passed for ENV_1 is " + env,severity="INFO")