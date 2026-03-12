# multithreading_basic.py
# Demonstrating basic multithreading in Python

import threading
import time


def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")


# Creating threads
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))
t3 = threading.Thread(target=task, args=("C",))

# Starting threads
t1.start()
t2.start()
t3.start()

# Waiting for threads to finish
t1.join()
t2.join()
t3.join()

print("All tasks completed....")