from decimal import Decimal


def btc(number: str):
    '''Converts a satoshi string to int value'''
    if number is not None:
        satoshi = Decimal(number)
        satoshi = satoshi * 100_000_000
        return int(satoshi)
    return None


def str_dec_int_conv(number: str):
    '''Converts a string to float to int'''
    if number is not None:
        number = Decimal(number)
        return int(number)
    return 0


def str_dec_conv(number: str):
    '''Converts a string decimal'''
    if number is not None:
        return Decimal(number)
    return 0
