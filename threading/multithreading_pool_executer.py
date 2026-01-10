###multithreading with pool executer

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"


numbers = [1,2,3,4,5,6,7,8,9,10]

t= time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)


for result in results:
    print(result)

print(f"Time taken: {time.time() - t} seconds")


###multithreading with pool executer
# it means we can run multiple threads at the same time using pool executer
###max_workers is the number of threads we want to run at the same time
# differnce between multithreading and with pool executer is that 
# in multithreading we have to create threads manually
# but in pool executer we can create threads automatically
# and we can also limit the number of threads we want to run at the same time
# here we are using max_workers=3 means we can run 3 threads at the same time
# so the total time taken will be 4 seconds instead of 10 seconds