from models.telegram_model import Telegram, cleanTelegramTables
from scrapers.currencies_page import parseCoinPageLinks
from scrapers.mainpage import getLinks
from utils.timeit import timeit
from utils.schedule_logger import with_logging

from time import sleep

import schedule
import logging
# logging.basicConfig(level=logging.INFO)


@timeit
@with_logging
def get_telegram_links(skip=0):

    coinmarketcap_links = getLinks()

    for idx, coin in enumerate(coinmarketcap_links):
        logging.info('\n')
        logging.info('Parsing: {}'.format(coin))

        if idx < skip:
            logging.info('skipping.')
            continue

        link = coinmarketcap_links[coin]

        parsed_data = parseCoinPageLinks(link)
        parsed_data['name'] = coin

        logging.debug(parsed_data)

        Telegram.addData(parsed_data)  # Added to Database

        logging.info('COMPLETED: {} out of {}.'.format(
            idx + 1, len(coinmarketcap_links)))

    logging.info('Telegram Data Cached')
    Telegram.cacheAllData()


def debug_test():
    # DEBUGGING SECTION
    url = 'https://coinmarketcap.com/currencies/ontology/'
    parsed = parseCoinPageLinks(url)
    parsed['name'] = 'coinmatic'
    print(parsed)

    dropTables()
    createTables()

    Telegram.addData(parsed)


def main():
    schedule.every().day.at('00:30').do(get_telegram_links)
    schedule.every().day.at('12:30').do(get_telegram_links)

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    # main()
    # get_telegram_links(skip=1595)
    # dropTables()
    # createTables()
    # debug_test()
    pass
