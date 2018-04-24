import logging

from scrapers.currencies_page import parseCoinPageLinks
from scrapers.mainpage import getLinks
from utils.timeit import timeit
from models.telegram_model import Telegram, cleanTelegramTables

logging.basicConfig(level=logging.INFO)


coinmarketcap_links = getLinks()


@timeit
def main(skip=0):

    for idx, coin in enumerate(coinmarketcap_links):
        logging.info('\n')
        logging.info('Parsing: {}'.format(coin))

        if idx < skip:
            logging.info('skipping.')
            continue

        link = coinmarketcap_links[coin]

        parsed = parseCoinPageLinks(link)
        parsed['name'] = coin
        logging.debug(parsed)

        Telegram.addData(parsed)  # Added to Database

        logging.info('COMPLETED: {} out of {}.'.format(
            idx + 1, len(coinmarketcap_links)))


def debug_test():
    # DEBUGGING SECTION
    url = 'https://coinmarketcap.com/currencies/ontology/'
    parsed = parseCoinPageLinks(url)
    parsed['name'] = 'coinmatic'
    print(parsed)

    dropTables()
    createTables()

    Telegram.addData(parsed)


if __name__ == '__main__':
    # dropTables()
    # createTables()
    main()
    # debug_test()
