# logging_example.py
# Demonstrating Python logging module

import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debugging information")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error occurred")
logging.critical("Critical issue detected")

print("Logging completed. Check app.log file.")