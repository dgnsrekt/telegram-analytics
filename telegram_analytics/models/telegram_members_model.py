import pandas as pd
import logging

from datetime import datetime
from peewee import *

from .base_model import BaseModel, db
from .telegram_model import Telegram


def getCurrentDateTime():
    return datetime.utcnow()


class TelegramMembers(BaseModel):
    name = CharField(null=True)
    telegram_link = ForeignKeyField(Telegram, to_field='telegram_link')
    members = BigIntegerField(null=True)
    created_date = DateTimeField()

    def addData(**kwargs):
        TelegramMembers.create(**kwargs)

        logging.info('New entry {} added to database.'.format(kwargs['name']))

    def getAllData():
        data = [[row.name, row.members, row.created_date]
                for row in TelegramMembers.select()]
        df = pd.DataFrame(data, columns=['name', 'members', 'date'])
        return data

    def pickleAllData(filename):
        data = [[row.name, row.members, row.created_date]
                for row in TelegramMembers.select()]
        df = pd.DataFrame(data, columns=['name', 'members', 'date'])
        df.to_pickle(filename)


def createTelegramMembersTables():
    db.create_tables([TelegramMembers])
    logging.info('(TelegramMembers) Tables Created')


def dropTelegramMembersTables():
    db.drop_tables([TelegramMembers])
    logging.info('(TelegramMembers) Tables Dropped')


def cleanTelegramMembersTables():
    dropTelegramMembersTables()
    createTelegramMembersTables()
