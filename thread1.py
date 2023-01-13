# thread1.c - Create two threads from a single process

import os
from threading import Thread, current_thread

def thread_function ():
    pid = os.getpid() # Get process ID
    tid = current_thread().name # Get thread name
    print("Hello from {} with PID = {}.".format(tid, pid))

if __name__ == "__main__":
    
    # Spawn two threads
    thread1 = Thread(target = thread_function)
    thread2 = Thread(target = thread_function)
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()
    