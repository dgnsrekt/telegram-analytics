from coinmarketcap import Market
# TODO: LOGGING


def getLinks(limit=None):
    url = 'https://coinmarketcap.com/currencies/{}'

    cap = Market()

    if not limit:
        stats = cap.stats()
        limit = stats['active_currencies'] + stats['active_assets']

    data = cap.ticker(limit=limit)

    pages = {}
    for coin in data:
        name = coin['id']
        link = url.format(coin['id'])

        pages[name] = link

    return pages
