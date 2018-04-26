import functools
import time

import schedule
import logging


# This decorator can be applied to
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Running job "{}"'.format(func.__name__))
        result = func(*args, **kwargs)
        logging.info('Job "{}" completed'.format(func.__name__))
        return result
    return wrapper
