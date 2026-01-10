#what is threading and multithreading?
# Threading is a technique that allows multiple threads to run concurrently within a single process.
# for example we can have multiple threads performing different tasks simultaneously.
# multithreading means using multiple threads within a single process to perform tasks concurrently.

# here more than one thread is accessing shared data. Locks can be used to ensure that only
#  one thread accesses the shared data at a time, preventing data corruption.
# threads are unit of execution within a process that can run concurrently.
#  In Python, the `threading` module provides a way to create and manage threads.

# when to use multithreading:
# 1. I/O-bound tasks: Multithreading is particularly useful for I/O-bound(taking more 
# time in input/output operations) tasks, such as file handling, network operations,
# concurrent web scraping, etc. While one thread is waiting for an I/O operation to complete, 


import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)#made the thread sleep for 1 second for simulating a time-consuming task
        print(f"Number: {i}")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1)
        print(f"Letter: {letter}")

## create two threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)


## record start time
t = time.time()
## start the threads
t1.start()
t2.start()

## wait for threads to complete
t1.join()
t2.join()
finished_time = time.time() - t
print(f"Time taken with multithreading: {finished_time} seconds")


