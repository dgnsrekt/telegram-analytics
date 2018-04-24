from model import Telegram
from scrapers.telegram import parseMemberCount
from scrapers.mainpage import getAllMarkets
from utils.timeit import timeit
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt

import logging
logging.basicConfig(level=logging.DEBUG)


@timeit
def main():
    df = Telegram.getAllTelegramNames()
    df.set_index('name', inplace=True)

    df2 = pd.DataFrame(getAllMarkets())
    df2.set_index('id', inplace=True)
    rslt = pd.concat([df, df2], axis=1, join_axes=[df.index])

    def f(x):
        sleep(0.01)
        logging.info('parsing {} telegram'.format(x['name']))
        return parseMemberCount(x['telegram_link'])

    rslt['members'] = rslt.apply(f, axis=1)
    col = ['percent_change_7d', 'percent_change_1h',
           'percent_change_24h', 'members']
    rslt[col] = rslt[col].apply(pd.to_numeric, errors='coerce')

    x = rslt['members'].groupby(rslt['symbol']).mean()
    y = rslt['percent_change_24h'].groupby(rslt['symbol']).max()
    y2 = rslt['percent_change_1h'].groupby(rslt['symbol']).max()
    y3 = rslt['percent_change_7d'].groupby(rslt['symbol']).max()

    print(x)
    print(y)

    plt.subplot2grid((2, 3), (0, 0))
    plt.scatter(x, y, c=y)
    plt.xlabel('Telegram Followers')
    plt.ylabel('Percent Change (24H)')

    plt.subplot2grid((2, 3), (1, 0))
    plt.scatter(x, y2, c=y2)
    plt.xlabel('Telegram Followers')
    plt.ylabel('Percent Change (1H)')

    plt.subplot2grid((2, 3), (1, 1))
    plt.scatter(x, y3, c=y3)
    plt.xlabel('Telegram Followers')
    plt.ylabel('Percent Change (7d)')

fig = plt.figure(figsize=(18, 9))
main()
plt.show()
