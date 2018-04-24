from requests_html import HTML, HTMLSession
from requests.exceptions import ConnectionError, ReadTimeout
from time import sleep

import logging


def cleanMemberCount(string):
    clean = string.replace('members', '')
    clean = clean.replace(' ', '')
    return int(clean)


def parseMemberCount(telegram_url):
    session = HTMLSession()
    logging.info('Connecting to {}'.format(telegram_url))
    response = session.get(telegram_url)

    if response.status_code == 200:
        text = response.html.text.split('\n')

        for line in text:
            if 'members' in line:
                try:
                    cleaned = cleanMemberCount(line)
                except ValueError:
                    cleaned = None
                logging.info('{} members found'.format(cleaned))
                return cleaned
        return None


# url = 'https://t.me/joinchat/GCeNfxAVLy6bo6VNR3a9hg'
# url = 'https://t.me/lendroidproject'
# url = 'https://t.me/joinchat/HVP0kBBx-murObE3hpv7HA'
# url = 'https://t.me/RaiWalletBot'
# url = 'https://t.me/StratisPlatform'
# url = 'https://t.me/joinchat/AAAAAEPriD4KXShTKx-Kpg'
# url = 'https://t.me/intelligenttradingbot'  # bad data
# url = 'https://t.me/intelligenttrading'
# print(parseMemberCount(url))
