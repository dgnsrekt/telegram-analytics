from telegram_analytics.scrapers.currencies_page import *


def test_isValidTelegramLink():
    assert isValidTelegramLink('https://t.me/') == True


def test_isValidTelegramLinkTwo():
    assert isValidTelegramLink('https://telegram.me/') == True


def test_isValidTelegramLinkThree():
    assert isValidTelegramLink('http://www.telegram.me/') == True


def test_isValidTelegramLinkFalse():
    assert isValidTelegramLink('www.google.com') == False
