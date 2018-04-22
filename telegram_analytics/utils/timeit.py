import time
import logging

from datetime import timedelta

logging.basicConfig(level=logging.DEBUG)


def pretty_time_delta(seconds):
    seconds = int(seconds)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        return '{:d}d{:d}h{:d}m{:d}s'.format(days, hours, minutes, seconds)
    elif hours > 0:
        return '{:d}h{:d}m{:d}s'.format(hours, minutes, seconds)
    elif minutes > 0:
        return '{:d}m{:d}s'.format(minutes, seconds)
    else:
        return '{:d}s'.format(seconds,)


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()

        delta = pretty_time_delta(end - start)
        logging.info('{} FUNCTION TIME: {}'.format(
            method.__name__.upper(), delta))
        return result
    return timed
