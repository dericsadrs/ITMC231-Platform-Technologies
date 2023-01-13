# thread2.py - Create two threads, each to perform a unique task.       

import os
import time
from threading import Thread, current_thread

def task1_sayhello(max_iterations):
    thread_id = current_thread().name
    for i in range(max_iterations):
        print("Hello from {}!".format(thread_id))
        time.sleep(1)

def task1_sayhi(max_iterations):
    thread_id = current_thread().name
    for i in range(max_iterations):
        print("Hi from {}!".format(thread_id))
        time.sleep(1)

if __name__ == "__main__":
    thread1 = Thread(target = task1_sayhello, args = (5,))
    thread2 = Thread(target = task1_sayhi, args = (10,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    