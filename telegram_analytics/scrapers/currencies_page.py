from requests_html import HTML, HTMLSession
import logging

logging.basicConfig(level=logging.DEBUG)


def elementIsWebsite(element):
    return element.attrs['title'] == 'Website'


def isValidTelegramLink(link):
    if 'https://t.me/' in link:
        return True
    elif 'https://telegram.me/' in link:
        return True
    elif 'http://www.telegram.me/' in link:
        return True


def parseCoinPageLinks(url):
    telegram_links = set()
    websites = set()
    session = HTMLSession()

    try:
        response = session.get(url)
        xpath = '/html/body/div[4]/div/div[1]/div[4]/div[2]/ul'
        ul = response.html.xpath(xpath)[0]
        spans = ul.find('span')
        links = ul.find('a')

        for span, li in zip(spans, links):
            link = li.links.pop()

            if elementIsWebsite(span):
                logging.debug('Found Website: {}'.format(link))
                websites.add(link)

            elif isValidTelegramLink(link):
                logging.debug('Found Telegram: {}'.format(link))
                telegram_links.add(link)

    except Exception as e:
        logging.error(e)
        raise

    logging.info('Parsed Websites:{}, Telegram:{}'.format(
        websites, telegram_links))

    return {'websites': websites, 'telegram_links': telegram_links}

url = 'https://coinmarketcap.com/currencies/tron/'
url = 'https://coinmarketcap.com/currencies/waltonchain/'
x = parseCoinPageLinks(url)
print(x)
