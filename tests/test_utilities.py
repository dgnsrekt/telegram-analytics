from telegram_analytics.utils.utilities import *


def test_btc():
    assert btc('0.0167122') == 1671220
    assert btc(0) == 0
    assert btc(None) == None
    assert btc(0.07129090) == 7129090


def test_str_dec_int_conv():
    assert str_dec_int_conv('0') == 0
    assert str_dec_int_conv(None) == 0
