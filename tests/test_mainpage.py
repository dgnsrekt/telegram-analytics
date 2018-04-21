from telegram_analytics.scrapers import mainpage


def test_getLinks():
    assert len(mainpage.getLinks(1)) == 1


def test_getLinks_2():
    assert mainpage.getLinks(
        1) == {'bitcoin': 'https://coinmarketcap.com/currencies/bitcoin'}
