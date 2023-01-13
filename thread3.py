# thread3.py - Create two threads sharing the same data and
#              restrict access to critical section using mutual exclusion lock     

import os
import time
from threading import Thread, current_thread, Lock

counter = 0 # Shared data

counter_lock = Lock() # Mutex lock

def sayhello(max_iterations):
    thread_id = current_thread().name
    
    # Lock the mutex. If already locked, the calling thread is suspended until mutex is unlocked
    counter_lock.acquire()

    # Critical section: counter is shared among threads
    global counter
    counter = 1
    while counter <= max_iterations:
        print("Loop {} of {}: Hello from {}!".format(counter, max_iterations, thread_id))
        time.sleep(1)
        counter = counter + 1

    # Unlock the mutex and wake the first thread sleeping on it
    counter_lock.release()

if __name__ == "__main__":
    
    # Spawn two threads
    thread1 = Thread(target = sayhello, args = (5,))
    thread2 = Thread(target = sayhello, args = (10,))
    
    print("Before: counter =", counter)
    thread2.start()
    thread1.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()
        
    print("After: counter =", counter)