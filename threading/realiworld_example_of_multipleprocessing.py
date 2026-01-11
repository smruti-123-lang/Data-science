#multiprocessing for cpu bound tasks
# scenario = factorial calculation
# cpu bound tasks are those that require significant 
# computational power and 
# spend most of their time utilizing the CPU


import multiprocessing
import math
import sys
import time

#inrease the maximum number of digits for integer conversion
sys.set_int_max_str_digits(1000000)# increase the limit to 1 million digits

##function to computr factorial


def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result


if __name__ == "__main__":
    numbers = [5000, 6000, 7000]

    start = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(compute_factorial, numbers)

    end = time.time()

print("the results are", results)
print("the finished time is", end - start)