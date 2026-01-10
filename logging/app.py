import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("arithmetic app")

def add(a, b):
    logger.debug(f"Adding {a} and {b} to get {a + b}")
    return a + b
def subtract(a, b):
    logger.debug(f"Subtracting {b} from {a} to get {a - b}")
    return a - b
def multiply(a, b):
    logger.debug(f"Multiplying {a} and {b} to get {a * b}")
    return a * b
def divide(a, b):
    if b == 0:
        logger.error("Attempted to divide by zero")
        return None
    logger.debug(f"Dividing {a} by {b} to get {a / b}")
    return a / b

add(10,15)
subtract(20,5)
divide(10,0)
multiply(3,7)