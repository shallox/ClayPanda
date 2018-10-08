from settings import conn_b, sql_warning
import time
import re


class MysqlPro:
    def make_table_bittrex(self):
        sql_warning
        tbl = self
        candles_tbl = "CREATE TABLE IF NOT EXISTS " + tbl + " (Market VARCHAR(10) NULL," \
                                                                      " O NUMERIC(20,10) NULL, H DECIMAL(20,10) NULL," \
                                                                      " L DECIMAL(20,10) NULL, C DECIMAL(20,10) NULL," \
                                                                      " V DECIMAL(32,16) NULL, T DATETIME NOT NULL," \
                                                                      " BV DECIMAL(20,10) NULL," \
                                                                      " PRIMARY KEY (T)) ENGINE = InnoDB DEFAULT" \
                                                                      " CHARACTER SET = utf8mb4 COLLATE" \
                                                                      " = utf8mb4_unicode_ci"
        with conn_b.cursor() as cur:
            cur.execute(candles_tbl)

    def ts_exist(self, candles_table, market_name):
        bittrex_dat = list(self)
        sql_warning
        with conn_b as cur:
            fetch_last = 'SELECT T FROM ' + candles_table + ' ORDER BY T DESC LIMIT 1'
            cur.execute(fetch_last)
            last_entry = cur.fetchone()
            if bittrex_dat is None:
                print('noting here', market_name)
            else:
                if last_entry is None:
                    print(last_entry, candles_table)
                    last_entry_final = 0
                else:
                    time_last = str(last_entry['T'])
                    last_entry_sub = re.sub('-|:|T', '', time_last)
                    last_entry_final = int(last_entry_sub.replace(' ', ''))
                for dat in bittrex_dat:
                    time_mod = int(re.sub('-|:|T', '', dat['T']))
                    candat_1 = dat['O']
                    candat_2 = dat['H']
                    candat_3 = dat['L']
                    candat_4 = dat['C']
                    candat_5 = dat['V']
                    candat_6 = dat['T']
                    candat_7 = dat['BV']
                    sql = "INSERT INTO " + candles_table + \
                          " (Market, O, H, L, C, V, T, BV)" \
                          " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    if time_mod > last_entry_final:
                        cur.execute(sql, (market_name, candat_1, candat_2, candat_3,
                                               candat_4, candat_5, candat_6, candat_7,))
                        time.sleep(.05)
                    else:
                        continue
