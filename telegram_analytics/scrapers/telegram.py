from requests_html import HTML, HTMLSession
from requests.exceptions import ConnectionError, ReadTimeout
from time import sleep

import logging

# logging.basicConfig(level=logging.DEBUG)


def cleanMemberCount(string):
    clean = string.replace('members', '')
    clean = clean.replace(' ', '')
    return int(clean)


def parseMemberCount(telegram_url):
    session = HTMLSession()
    response = session.get(url)

    if response.status_code == 200:
        text = response.html.text.split('\n')

        for line in text:
            if 'members' in line:
                cleaned = cleanMemberCount(line)
                logging.info('{} members found'.format(cleaned))
                return cleaned


# url = 'https://t.me/joinchat/GCeNfxAVLy6bo6VNR3a9hg'
# url = 'https://t.me/lendroidproject'
# url = 'https://t.me/joinchat/HVP0kBBx-murObE3hpv7HA'
# url = 'https://t.me/RaiWalletBot'
# url = 'https://t.me/StratisPlatform'
# url = 'https://t.me/joinchat/AAAAAEPriD4KXShTKx-Kpg'
# parseMemberCount(url)
