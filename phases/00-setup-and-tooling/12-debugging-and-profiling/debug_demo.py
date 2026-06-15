# debug_demo.py
import logging

logging.basicConfig(level=logging.CRITICAL, format='%(levelname)s - %(message)s')

def divide(a, b):
    logging.debug(f"divide called with a={a}, b={b}")
    if b == 0:
        logging.error("Division by zero attempted!")
        return None
    result = a / b
    logging.info(f"Result: {result}")
    return result

divide(10, 2)
divide(5, 0)
