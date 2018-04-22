from requests_html import HTML, HTMLSession
from requests.exceptions import ConnectionError, ReadTimeout
from time import sleep

import logging

# logging.basicConfig(level=logging.DEBUG)


def elementIsWebsite(element):
    return element.attrs['title'] == 'Website'


def isValidTelegramLink(link):
    if 'https://t.me/' in link:
        return True
    elif 'https://telegram.me/' in link:
        return True
    elif 'http://www.telegram.me/' in link:
        return True


# TODO: retry decorator that sleeps and retrys using audacity
def parseCoinsMainPageTelegramLinks(_link):
    telegram_links = list()
    session = HTMLSession()
    logging.debug('Parsing the sponsored page: {}'.format(_link))

    try:
        response = session.get(_link, timeout=1)
        if response.status_code != 200:
            logging.error('{} Code: {}'.format(response.status_code, _link))
            return telegram_links

        for link in response.html.links:
            if isValidTelegramLink(link):
                logging.debug('Found Telegram(Sponsor Page): {}'.format(link))
                telegram_links.append(link)

        return telegram_links

    except ConnectionError as e:
        logging.error(e)

    except ReadTimeout as e:
        logging.error(e)

    except ValueError as e:
        logging.error(e)

    except Exception as e:
        logging.error(e)
        raise


# TODO: retry decorator that sleeps and retrys using audacity


def parseCoinPageLinks(url):
    telegram_links = set()
    websites = set()
    session = HTMLSession()

    try:
        response = session.get(url)
        if response.status_code != 200:
            raise Exception('{}'.format(response.status_code))
            # TODO: Add error to retry on this connection error

        sel = 'body > div.container > div > div.col-lg-10 > div.row.bottom-margin-2x > div.col-sm-4.col-sm-pull-8 > ul'
        ul = response.html.find(sel)

        spans = ul[0].find('span')
        links = ul[0].find('a')

        for span, li in zip(spans, links):
            try:
                link = li.links.pop()

            except KeyError as e:
                print(e)
                link = set()

            if isValidTelegramLink(link):
                logging.debug('Found Telegram: {}'.format(link))
                telegram_links.add(link)

            elif elementIsWebsite(span):
                logging.debug('Found Website: {}'.format(link))
                websites.add(link)
                parse_telegram_links = parseCoinsMainPageTelegramLinks(link)
                sleep(1)

                if parse_telegram_links:
                    telegram_links.update(parse_telegram_links)

    except IndexError as e:
        logging.error(e)
        raise

    except Exception as e:
        logging.error(e)
        raise

    logging.info('Parsed Websites:{}, Telegram:{}'.format(
        websites, telegram_links))

    return {'websites': websites, 'telegram_links': telegram_links}
