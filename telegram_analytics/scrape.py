import logging

from scrapers.currencies_page import parseCoinPageLinks
from scrapers.mainpage import getLinks
from utils.timeit import timeit

logging.basicConfig(level=logging.DEBUG)


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

        parseCoinPageLinks(link)

        logging.info('COMPLETED: {} out of {}.'.format(
            idx + 1, len(coinmarketcap_links)))

if __name__ == '__main__':
    main()

    # DEBUGGING SECTION
    # url = 'http://coimatic.com/'
    # parseCoinPageLinks(url)
