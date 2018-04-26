
from models.telegram_model import Telegram, TelegramCacheError
from models.telegram_members_model import TelegramMembers, getCurrentDateTime
from models.telegram_members_model import cleanTelegramMembersTables  # DEBUG DELETE
from scrapers.telegram import parseMemberCount
from scrapers.mainpage import getAllMarkets, getCoinData
from utils.timeit import timeit
from utils.schedule_logger import with_logging
from utils.utilities import *

from datetime import datetime
from time import sleep, time

import schedule

import logging
logging.basicConfig(level=logging.INFO)


@timeit
@with_logging
def sample_telegram_member_count(tail=None):
    try:
        dataframe = Telegram.getAllCachedData()
    except TelegramCacheError as e:
        logging.warning(e)
        logging.info('Ending this session')
        return None

    if tail:
        dataframe = dataframe.tail(tail)

    dataframe_len = len(dataframe)
    created_date = getCurrentDateTime()

    for idx, row in enumerate(dataframe.iterrows()):
        name = row[1]['name']
        link = row[1]['telegram_link']
        members = parseMemberCount(link)

        coinmarketcap_data = getCoinData(name)
        print(coinmarketcap_data.get('market_cap_usd', 0))
        print('vol', coinmarketcap_data.get('24h_volume_usd', 0))

        price_usd = str_dec_conv(coinmarketcap_data.get('price_usd', 0))
        price_btc = btc(coinmarketcap_data.get('price_btc', 0))
        volume = str_dec_int_conv(coinmarketcap_data.get('24h_volume_usd', 0))
        marketcap = str_dec_int_conv(coinmarketcap_data.get('market_cap_usd', 0))

        data = {'name': name,
                'telegram_link': link,
                'members': members,
                'price_usd': price_usd,
                'price_btc': price_btc,
                'volume': volume,
                'marketcap': marketcap,
                'created_date': created_date}

        TelegramMembers.addData(**data)
        logging.info('COMPLETED: {} out of {}\n'.format(idx + 1, dataframe_len))
    logging.info('TIME: {}'.format(datetime.now()))  # move to timeit


def main():
    # schedule.every().minute.do(sample_telegram_member_count, tail=5)  # debugger
    for idx in range(24):
        time = '{:02d}:00'.format(idx)
        schedule.every().day.at(time).do(sample_telegram_member_count)

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    # DEBUG DELETE WHEN DONE
    # cleanTelegramMembersTables()
    # sample_telegram_member_count(tail=10)
    # main()
    pass
