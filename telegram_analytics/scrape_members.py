
from models.telegram_model import Telegram
from models.telegram_members_model import TelegramMembers, getCurrentDateTime
from models.telegram_members_model import cleanTelegramMembersTables  # DEBUG DELETE
from scrapers.telegram import parseMemberCount
from scrapers.mainpage import getAllMarkets
from utils.timeit import timeit
from time import sleep

import schedule

import logging
logging.basicConfig(level=logging.DEBUG)

# DEBUG DELETE WHEN DONE
cleanTelegramMembersTables()


@timeit
def sample_telegram_member_count(tail=None):
    if tail:
        dataframe = Telegram.getAllTelegramNames().tail(tail)
    else:
        dataframe = Telegram.getAllTelegramNames()

    dataframe_len = len(dataframe)
    created_date = getCurrentDateTime()

    for idx, row in enumerate(dataframe.iterrows()):
        name = row[1]['name']
        link = row[1]['telegram_link']
        members = parseMemberCount(link)

        data = {'name': name,
                'telegram_link': link,
                'members': members,
                'created_date': created_date}

        TelegramMembers.addData(**data)
        logging.info('COMPLETED: {} out of {}\n'.format(idx + 1, dataframe_len))


def main():
    schedule.every(1).hours.do(sample_telegram_member_count)

    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main()
