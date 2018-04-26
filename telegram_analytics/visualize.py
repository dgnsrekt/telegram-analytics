from models.telegram_members_model import TelegramMembers
from scrapers.mainpage import getAllMarkets
from utils.timeit import timeit
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt

import logging
logging.basicConfig(level=logging.INFO)

# TelegramMembers.pickleAllData('members.pickle')
df = pd.read_pickle('members.pickle')
print(df.head())
print(df.describe())
print(df.info())

df.dropna(inplace=True)
df.set_index('name', inplace=True)

start = df.date.unique().min()
end = df.date.unique().max()

start_df = df[df.date == start]
end_df = df[df.date == end]

start_series = start_df['members'].groupby(start_df.index).median()
end_series = end_df['members'].groupby(end_df.index).median()

change = end_series - start_series
print(change.sort_values())

marketdata = getAllMarkets()
bitcoin_price = float(marketdata[0].get('price_usd'))

df2 = pd.DataFrame(marketdata)
df2['name'] = df2.id
df2.set_index('name', inplace=True)
cols = ['percent_change_1h', 'percent_change_24h',
        'percent_change_7d', '24h_volume_usd', 'market_cap_usd']
df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')
df2 = df2[cols]
print(df2.head())
change = change.to_frame()
final = pd.concat([change, df2], axis=1, join_axes=[change.index])
final = final[final['24h_volume_usd'] > bitcoin_price]
final = final[final['members'] > 0]
print(final.describe())
print(final.info())


data_1h = final[['members', 'percent_change_1h']].dropna()
data_24h = final[['members', 'percent_change_24h']].dropna()
data_7d = final[['members', 'percent_change_7d']].dropna()

fig = plt.figure(figsize=(18, 9))

x = data_1h.members
y = data_1h.percent_change_1h
plt.subplot2grid((2, 3), (0, 0))
plt.scatter(x, y, c=y)
plt.xlabel('change in members')
plt.ylabel('1h percent change')

x = data_24h.members
y = data_24h.percent_change_24h
plt.subplot2grid((2, 3), (0, 1))
plt.scatter(x, y, c=y)
plt.xlabel('change in members')
plt.ylabel('24h percent change')

x = data_7d.members
y = data_7d.percent_change_7d
plt.subplot2grid((2, 3), (1, 0))
plt.scatter(x, y, c=y)
plt.xlabel('change in members')
plt.ylabel('7d percent change')

most_members_gained = data_1h.sort_values('members').tail(10)
plt.subplot2grid((2, 3), (1, 1))
most_members_gained.members.plot(kind='bar', subplots=True)
plt.show()


# print(df[df.index == 'gpu-coin'])
