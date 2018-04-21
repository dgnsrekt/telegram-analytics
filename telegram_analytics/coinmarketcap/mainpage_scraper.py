from coinmarketcap import Market
# TODO: LOGGING


def getLinks(limit=None):
    url = 'https://coinmarketcap.com/currencies/{}'

    cap = Market()

    if not limit:
        stats = cap.stats()
        active_crypto = stats['active_currencies'] + stats['active_assets']
        limit = active_crypto

    data = cap.ticker(limit=limit)

    pages = {}
    for coin in data:
        name = coin['id']
        link = url.format(coin['id'])

        # print()
        # print('=' * 10)
        # print(name, link)

        pages[name] = link

    return pages
