from logger import logging

def add(a, b):
    logging.debug(f'Adding {a} and {b}')
    return a + b

logging.info('Test module started')
add(10,15)
