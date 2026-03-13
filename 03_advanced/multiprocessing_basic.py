# multiprocessing_basic.py
# Demonstrating basic multiprocessing in Python

from multiprocessing import Process
import os

def task(name):
    print(f"Process {name} running with PID:", os.getpid())


if __name__ == "__main__":
    p1 = Process(target=task, args=("A",))
    p2 = Process(target=task, args=("B",))
    p3 = Process(target=task, args=("C",))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("All processes completed....")