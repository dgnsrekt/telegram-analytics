import pandas as pd
import logging

from datetime import datetime
from peewee import *
from .base_model import BaseModel, db


class TelegramCacheError(Exception):
    pass


def getCurrentDateTime():
    return datetime.utcnow()


class Telegram(BaseModel):
    name = CharField(null=True)

    telegram_link = CharField(null=False, unique=True)

    created_date = DateTimeField()

    def addData(kwargs):
        links = kwargs['telegram_links']

        for link in links:
            try:
                Telegram.create(**{'name': kwargs['name'],
                                   'telegram_link': link,
                                   'created_date': getCurrentDateTime()})
                logging.info(
                    'New entry {} added to database.'.format(kwargs['name']))
            except IntegrityError:
                db.rollback()
                logging.info('{} already exists'.format(link))

    def getAllData():
        df = pd.DataFrame(list(Telegram.select().dicts()))
        return df

    def cacheAllData():
        filename = 'Telegram.cache'  # TODO add to config
        df = pd.DataFrame(list(Telegram.select().dicts()))
        df.to_pickle(filename)
        logging.info(f'{filename} created')

    def getAllCachedData():
        filename = 'Telegram.cache'  # TODO add to config
        try:
            df = pd.read_pickle(filename)
        except FileNotFoundError:
            raise TelegramCacheError('Telegram database cache not found.')
        else:
            logging.info('Telegram.cache read.')
            return df


def createTelegramTables():
    db.create_tables([Telegram])
    logging.info('Tables Created')


def dropTelegramTables():
    db.drop_tables([Telegram])
    logging.info('Tables Dropped')


def cleanTelegramTables():
    dropTelegramTables()
    createTelegramTables()
