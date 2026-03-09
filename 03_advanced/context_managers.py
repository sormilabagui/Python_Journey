# context_managers.py
# Demonstrating custom context managers in Python

class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Opening log file...")
        self.file = open(self.filename, "a")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing log file...")
        self.file.close()

# Using the custom context manager
with FileLogger("activity_log.txt") as log:
    log.write("Python advanced concepts practiced today.\n")
    log.write("Context manager example executed successfully.\n")

print("Logging completed")