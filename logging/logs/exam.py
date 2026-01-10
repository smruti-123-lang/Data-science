from logger import logging

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero.", exc_info=True)
        return None