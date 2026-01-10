##processses that run in parallel, each with its own Python interpreter and memory space.
# This is particularly useful for CPU-bound tasks (taking more time in computations),
# parallel execution multiple cores of a CPU can be utilized effectively.


# difference between multithreading and multiprocessing:
# 1. Memory Usage: Multithreading uses less memory as threads share the same memory space,
# whereas multiprocessing requires separate memory space for each process, leading to higher memory consumption.
# 2. Communication: Inter-thread communication is easier and faster as threads share the same memory,
# while inter-process communication (IPC) is more complex and slower due to separate memory spaces.
# 3. Overhead: Creating and managing threads has lower overhead compared to processes,
# making multithreading more efficient for I/O-bound tasks. Multiprocessing has higher overhead due
# to process creation and context switching, but it is more effective for CPU-bound tasks.


import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"cube:{i*i*i}")


if __name__ == "__main__":#main module check to ensure that the code runs only when the script is executed directly
    t1 = time.time()
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    t2 = time.time()
    print(f"Total time taken: {t2 - t1}")