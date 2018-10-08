import settings
from txt_scan import TxtScan
from calc import Calc


class RedditSearch():
    def reddit_std(self, t_name, b_cur, m_cur):
        r_num = 0
        r_search = t_name, self, m_cur
        reddit_stream = settings.reddit.subreddit\
            ('icocrypto+Trading+CryptoCurrency+cryptotrader+Bitcoin+ethereum+Bittrex+CryptoMarkets+BitcoinAll').\
            search(r_search, time_filter='hour', limit=1000)
        for submission in reddit_stream:
            r_num +=1
            #process_submission(submission)
            #srch = reddit.subreddits.search(subst)
            #sub_id = submission.id
            #sub_red = submission.subreddit.display_name
            subtit = submission.title
            #sub_url = submission.url
            #sub_scr = submission.score
            sub_ups = submission.ups
            sub_dwn = submission.downs
            #stl = submission.title.lower()
            scl = submission.comments.replace_more(limit=None, threshold=0)
            #san = submission.author
            TxtScan.text_scan_reddit(subtit, sub_dwn, sub_ups)
            for comment in scl:
                r_num += 1
                sub_ups = comment.ups
                sub_dwn = comment.downs
                TxtScan.text_itr_scan_reddit(comment.body, sub_dwn, sub_ups)
        if r_num <= 0:
            return
        else:
            tb_name = 'analysis_' + b_cur + '_' + m_cur
            Calc.calc_reddit(tb_name, t_name)
            return #print('---- Done scanning Reddit', t_name, '----')


class Reddit_serch_itter():
    def reddit_refine(self, t_name, b_cur, m_cur):
        main_list = []
        r_num = 0
        r_search = t_name, self, m_cur
        reddit_stream = settings.reddit.subreddit('icocrypto+Trading+CryptoCurrency+cryptotrader+Bitcoin+ethereum+'
                                                  'Bittrex+CryptoMarkets+BitcoinAll').\
            search(r_search)#, limit=1000)#, time_filter='hour')
        for submission in reddit_stream:
            r_num += 1
            subtit = submission.title
            sub_ups = submission.ups
            sub_dwn = submission.downs
            scl = submission.comments.replace_more(limit=None, threshold=0)
            data_point = {'title': subtit, 'up': sub_ups, 'dwn': sub_dwn}
            main_list.append(data_point)
            for comment in scl:
                r_num += 1
                sub_ups = comment.ups
                sub_dwn = comment.downs
                data_point = {'title': subtit, 'up': sub_ups, 'dwn': sub_dwn}
                main_list.append(data_point)
        if r_num <= 0:
            return
        else:
            tb_name = 'iter_analysis_' + b_cur + '_' + m_cur
            TxtScan.multi_reddit(main_list, t_name, tb_name, r_num)
