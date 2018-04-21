from telegram_analytics.coinmarketcap import mainpage_scraper


def test_getLinks():
    assert len(mainpage_scraper.getLinks(1)) == 1


def test_getLinks_2():
    assert mainpage_scraper.getLinks(
        1) == {'bitcoin': 'https://coinmarketcap.com/currencies/bitcoin'}
