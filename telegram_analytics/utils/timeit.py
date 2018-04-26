import time
import logging

from datetime import timedelta


def prettyTimeDelta(seconds):
    seconds = int(seconds)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        return f'{days:}d{hours:}h{minutes:}m{seconds:}s'
    elif hours > 0:
        return f'{hours:}h{minutes:}m{seconds:}s'
    elif minutes > 0:
        return f'{minutes:}m{seconds:}s'
    else:
        return f'{seconds:}s'


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()

        delta = prettyTimeDelta(end - start)
        logging.info('{} FUNCTION TOOK {} TO COMPLETE.'.format(
            method.__name__.upper(), delta))
        return result
    return timed
