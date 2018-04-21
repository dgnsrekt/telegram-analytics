from telegram_analytics.scrapers.currencies_page import *


def test_isValidTelegramLink():
    assert isValidTelegramLink('https://t.me/') == True
