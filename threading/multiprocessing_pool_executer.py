from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square of {number} is {number * number}"

numbers = [1,23,45,67,89,12,34,56,78,90]

if __name__ == "__main__":
    start = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)

    end = time.time()
    print(f"\nTotal execution time: {end - start:.2f} seconds")
