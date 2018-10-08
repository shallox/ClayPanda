import brex
import reddit
import multiprocessing
import time
import os
import logging
from settings import refine_reddit


logging.basicConfig(filename=os.path.join(os.getcwd(), 'error.log'), level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)



def main():
    main_pid = os.getpid()
    star_time = time.asctime(time.localtime(time.time()))
    print('---- Starting market scan', star_time, 'ID=', main_pid, '----')
    total_markets = 0
    total_markets_run = 0
    for b in brex.Marrkt.bnb:
        total_markets += 1
    for a in brex.Marrkt.bnb:
        if a['IsActive'] is False:
            continue
        else:
            total_markets_run += 1
            mrk = a['MarketCurrencyLong']
            #bmrk = a['BaseCurrencyLong']
            t_name = a['MarketName']
            b_cur = a['BaseCurrency']
            m_cur = a['MarketCurrency']
            if refine_reddit is True:
                r_search = multiprocessing.Process(target=reddit.Reddit_serch_itter.reddit_refine,
                                                   args=(mrk, t_name, b_cur, m_cur))
                r_search.daemon = True
                r_search.start()
                time.sleep(60)
            else:
                r_search = multiprocessing.Process(target=reddit.RedditSearch.reddit_std, args=(mrk, t_name, b_cur, m_cur))
                b_candles = multiprocessing.Process(target=brex.Marrkt.get_candles, args=(t_name,))
                r_search.daemon = True
                b_candles.daemon = True
                r_search.start()
                b_candles.start()
            run_percent = int(100 * float(total_markets_run) / float(total_markets))
            #print('---- Progress', str(run_percent) + '%', 'starting', t_name, '----')
            time.sleep(4)
    still_live()


def still_live():
    retry_count = 0
    running_count = multiprocessing.active_children()
    num_run = 0
    for c in running_count:
        num_run += 1
    if num_run == 0:
        return print('---- Done @' + time.asctime(time.localtime(time.time())) + ' ----')
    else:
        if retry_count >= 8:
            return print('---- Done @' + time.asctime(time.localtime(time.time())) + ' ----')
        else:
            retry_count += 1
            print('---- Still working - running processes =', num_run, '----')
            time.sleep(30)
            still_live()


if __name__ == '__main__':
    main()
