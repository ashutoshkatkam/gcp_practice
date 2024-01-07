# This is the version 1 code

import os
import logging
import sys

logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')


# Instantiates a client
# client = logging.Client(project="my-project")
# logger = client.logger(name="my_app1_logs")

logging.info("Version 1 application started")

# parser = argparse.ArgumentParser(description="Read and print the file name")
# parser.add_argument("filename", help="The name of the file to read.")
# args = parser.parse_args()

# Display the file name passed to the code
logging.info("Passed filename is "+ sys.argv[1])


# Reading the passed environemnt variable of the container.
env = os.environ.get('ENV_1')

# Logging the environment variable of the container.
logging.info("Environment variable passed for ENV_1 is " + env)