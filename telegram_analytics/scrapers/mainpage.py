from coinmarketcap import Market
# TODO: LOGGING


def getAllMarkets(limit=None):
    cap = Market()

    if not limit:
        stats = cap.stats()
        limit = stats['active_currencies'] + stats['active_assets']

    return cap.ticker(limit=limit)


def getLinks(limit=None):
    url = 'https://coinmarketcap.com/currencies/{}'

    data = getAllMarkets(limit)

    pages = {}
    for coin in data:
        name = coin['id']
        link = url.format(coin['id'])

        pages[name] = link

    return pages


def getCoinData(coin):
    cap = Market()

    data = cap.ticker(coin)
    if data == {'error': 'id not found'}:
        return None
    return data[0]
