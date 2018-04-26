from coinmarketcap import Market
from .utilities import *


class CoinData():

    def __init__(self, coin):
        self.market = Market()
        self.coin = coin
        self.data = self.getData()

    def getData(self):
        data = self.market.ticker(self.coin)
        if data == {'error': 'id not found'}:
            return None
        else:
            return data[0]

    @property
    def price_usd(self):
        price_usd = self.data.get('price_usd', 0)
        price_usd = str_dec_conv(price_usd)
        return price_usd

    @property
    def price_btc(self):
        price_btc = self.data.get('price_btc', 0)
        return btc(price_btc)

    @property
    def volume(self):
        volume = self.data.get('24h_volume_usd', 0)
        return str_dec_int_conv(volume)

    @property
    def marketcap(self):
        marketcap = self.data.get('market_cap_usd', 0)
        return str_dec_int_conv(marketcap)

    def __str__(self):
        return str(self.data)


# x = CoinData('litecoin')
# print(x.price_usd, type(x.price_usd))
# print(x.price_btc, type(x.price_btc))
# print(x.volume, type(x.volume))
# print(x.marketcap, type(x.marketcap))
