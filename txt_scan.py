from textblob import TextBlob
from calc import Scoring, Calc
import multiprocessing as mpr
import time
from itertools import product


class TxtScan():
    def text_scan_reddit(self, sub_dwn, sub_ups):
        Scoring.total_data_points +=1
        sa = TextBlob(self)
        t_sent = sa.sentiment
        if t_sent.polarity <= -0.01 and t_sent.subjectivity > 0.16:
            Scoring.no_score += 1
            Scoring.nu_score += int(sub_ups)
            Scoring.nd_score += int(sub_dwn)
        elif t_sent.polarity <= -0.01 and t_sent.subjectivity <= 0.16:
            Scoring.nf_score += 1
            Scoring.nu_score += int(sub_ups)
            Scoring.nd_score += int(sub_dwn)
        elif t_sent.subjectivity < 0.3:
            Scoring.pf_score += 1
            Scoring.pu_score += int(sub_ups)
            Scoring.pd_score += int(sub_dwn)
        elif t_sent.subjectivity >= 0.3:
            Scoring.po_score += 1
            Scoring.pu_score += int(sub_ups)
            Scoring.pd_score += int(sub_dwn)


    def iterval_polarity():
        start = True
        pol_num = 9
        polarity_numbers = []
        polarity_floats = []

        while start is True:
            if pol_num >= 99:
                start = False
            else:
                pol_num += 2
                polarity_numbers.append(pol_num)
        for a in polarity_numbers:
            neg = '-0.' + str(a)
            polarity_floats.append(round(float(neg), 2))
        for b in polarity_numbers:
            pos = '0.' + str(b)
            polarity_floats.append(round(float(pos), 2))
        return polarity_floats

    def iterval_subjectivity():
        start = True
        pol_num = 9
        polarity_numbers = []
        polarity_floats = []

        while start is True:
            if pol_num >= 99:
                start = False
            else:
                pol_num += 1
                polarity_numbers.append(pol_num)
        for a in polarity_numbers:
            pos = '0.' + str(a)
            polarity_floats.append(round(float(pos), 2))
        return polarity_floats


    def multi_reddit(self, t_name, tb_name, r_num):
        a = list(product(TxtScan.iterval_polarity(), TxtScan.iterval_subjectivity()))
        for b in a:
            c_num = 0
            for c in b:
                if c_num <= 0:
                    c_num +=1
                    f = c
                else:
                    b = c
            time.sleep(.5)
            spawn_pro = mpr.Process(target=TxtScan.text_itr_scan_reddit, args=(self, t_name, tb_name, f, b, r_num))
            spawn_pro.daemon = True
            spawn_pro.run()
        TxtScan.still_live()


    def still_live():
        running_count = mpr.active_children()
        num_run = 0
        for c in running_count:
            num_run += 1
        if num_run == 0:
            return
        else:
            time.sleep(30)
            TxtScan.still_live()


    def text_itr_scan_reddit(self, t_name, tb_name, f, b, r_num):
        total_data_points = r_num
        po_score = 0
        pf_score = 0
        no_score = 0
        nf_score = 0
        nu_score = 0
        nd_score = 0
        pu_score = 0
        pd_score = 0
        dat_point = list(self)
        for a in dat_point:
            txt = a['title']
            sub_ups = a['up']
            sub_dwn = a['dwn']
            sa = TextBlob(txt)
            t_sent = sa.sentiment
            if t_sent.polarity <= f and t_sent.subjectivity > b:
                no_score += 1
                nu_score += int(sub_ups)
                nd_score += int(sub_dwn)
            elif t_sent.polarity <= f and t_sent.subjectivity <= b:
                nf_score += 1
                nu_score += int(sub_ups)
                nd_score += int(sub_dwn)
            elif t_sent.subjectivity < b:
                pf_score += 1
                pu_score += int(sub_ups)
                Scoring.pd_score += int(sub_dwn)
            elif t_sent.subjectivity >= b:
                po_score += 1
                pu_score += int(sub_ups)
                pd_score += int(sub_dwn)
        Calc.calc_reddit_ittr(tb_name, t_name, f, b, total_data_points, po_score, pf_score,
                              no_score, nf_score, nu_score, nd_score, pu_score, pd_score)