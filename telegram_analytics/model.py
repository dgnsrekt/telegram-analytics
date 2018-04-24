import pandas as pd
import logging

from datetime import datetime
from peewee import *


db = PostgresqlDatabase('telegram')


def getCurrentDateTime():
    return datetime.utcnow()


class BaseModel(Model):

    class Meta:
        database = db


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

    def getAllTelegramNames():
        df = pd.DataFrame(list(Telegram.select().dicts()))
        # df.set_index('name', inplace=True)
        return df


def createTables():
    db.create_tables([Telegram])
    logging.info('Tables Created')


def dropTables():
    db.drop_tables([Telegram])
    logging.info('Tables Dropped')
