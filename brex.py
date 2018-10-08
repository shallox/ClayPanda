from settings import brexv1, brexv2
import mysql_process


class Marrkt():
    bnb = dict.get(brexv1.get_markets(), 'result')

    def get_candles(self):
        market_name = self
        candles_table = 'bittrex_candles_' + str(self).replace('-', '_')
        mysql_process.MysqlPro.make_table_bittrex(candles_table)
        market_cand = brexv2.get_candles(market=market_name, tick_interval='hour')
        candle_main = market_cand['result']
        if candle_main is None:
            print(market_name, 'has no data.')
        else:
            mysql_process.MysqlPro.ts_exist(candle_main, candles_table, market_name)
        return #print('---- Done scanning Bittrex', self, '----')
