from settings import conn_r, sql_warning, conn_refine


sql_warning


class Scoring():
    ups = 0
    downs = 0
    po_score = 0
    pf_score = 0
    no_score = 0
    nf_score = 0
    nu_score = 0
    nd_score = 0
    pu_score = 0
    pd_score = 0
    total_data_points = 0


class Calc():
    def calc_reddit(self, t_name):
        ps_total = Scoring.po_score + Scoring.pf_score
        ns_total = Scoring.nf_score + Scoring.no_score
        v_total = (Scoring.pu_score + Scoring.nu_score) + (Scoring.pd_score + Scoring.nd_score)
        if Scoring.pf_score > 0:
            positive_statement = 100 * float(Scoring.pf_score) / float(Scoring.total_data_points)
        else:
            positive_statement = 0.00
        ## Positive Statment calculation ##
        if Scoring.po_score > 0:
            positive_opinions = 100 * float(Scoring.po_score) / float(Scoring.total_data_points)
        else:
            positive_opinions = 0.00
        ## Negative Statment calculation ##
        if Scoring.nf_score > 0:
            negative_statement = 100 * float(Scoring.nf_score) / float(Scoring.total_data_points)
        else:
            negative_statement = 0.00
        ## Negative Opinion calculation ##
        if Scoring.no_score > 0:
            negative_opinion = 100 * float(Scoring.no_score) / float(Scoring.total_data_points)
        else:
            negative_opinion = 0.00
        ## Calculation of total data points vs amount of positive to negative text clasifications ##
        if Scoring.nu_score > 0:
            negative_positive = 100 * float(Scoring.nu_score) / float(v_total)
        else:
            negative_positive = 0.00
        if Scoring.nd_score > 0:
            negative_negative = 100 * float(Scoring.nd_score) / float(v_total)
        else:
            negative_negative = 0.00
        if Scoring.pu_score > 0:
            positive_positive = 100 * float(Scoring.pu_score) / float(v_total)
        else:
            positive_positive = 0.00
        if Scoring.pd_score > 0:
            positive_negative = 100 * float(Scoring.pd_score) / float(v_total)
        else:
            positive_negative = 0.00
            ## Calculation of total data points vs amount of positive to negative text clasifications ##
        overall_positive = 100 * float(ps_total) / float(Scoring.total_data_points)
        overall_negative = 100 * float(ns_total) / float(Scoring.total_data_points)
        with conn_r.cursor() as cur:
            t_make = "CREATE TABLE IF NOT EXISTS " + self + " (time_stamp_now TIMESTAMP NULL" \
                                                              " DEFAULT CURRENT_TIMESTAMP," \
                                                              " id INT(30) NOT NULL AUTO_INCREMENT," \
                                                              " currency_name VARCHAR(255) NULL," \
                                                              " total_data_points INT(20) NULL," \
                                                              " positive_statement DECIMAL(20,10) NULL," \
                                                              " positive_opinions DECIMAL(20,10) NULL," \
                                                              " negative_statement DECIMAL(20,10) NULL," \
                                                              " negative_opinion DECIMAL(20,10) NULL," \
                                                              " overall_positive DECIMAL(20,10) NULL," \
                                                              " overall_negative DECIMAL(20,10) NULL," \
                                                              " negative_positive DECIMAL(20,10) NULL," \
                                                              " negative_negative DECIMAL(20,10) NULL," \
                                                              " positive_positive DECIMAL(20,10) NULL," \
                                                              " positive_negative DECIMAL(20,10) NULL," \
                                                              " PRIMARY KEY (id)) ENGINE = InnoDB" \
                                                              " DEFAULT CHARACTER SET = utf8mb4" \
                                                              " COLLATE = utf8mb4_unicode_ci"

            t_add = "INSERT INTO " + self + "(currency_name, total_data_points, negative_positive," \
                                              " negative_negative, positive_positive, positive_negative," \
                                              " positive_statement, positive_opinions, negative_statement," \
                                              " negative_opinion, overall_positive, overall_negative)" \
                                              " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(t_make)
            cur.execute(t_add, (t_name, Scoring.total_data_points, negative_positive,
                                negative_negative, positive_positive, positive_negative,
                                positive_statement, positive_opinions, negative_statement,
                                negative_opinion, overall_positive, overall_negative,))


    def calc_reddit_ittr(self, t_name, f, b, total_data_points, po_score, pf_score,
                         no_score, nf_score, nu_score, nd_score, pu_score, pd_score):
        ps_total = po_score + pf_score
        ns_total = nf_score + no_score
        v_total = (pu_score + nu_score) + (pd_score + nd_score)
        if pf_score > 0:
            positive_statement = 100 * float(pf_score) / float(total_data_points)
        else:
            positive_statement = 0.00
        ## Positive Statment calculation ##
        if po_score > 0:
            positive_opinions = 100 * float(po_score) / float(total_data_points)
        else:
            positive_opinions = 0.00
        ## Negative Statment calculation ##
        if nf_score > 0:
            negative_statement = 100 * float(nf_score) / float(total_data_points)
        else:
            negative_statement = 0.00
        ## Negative Opinion calculation ##
        if no_score > 0:
            negative_opinion = 100 * float(no_score) / float(total_data_points)
        else:
            negative_opinion = 0.00
        ## Calculation of total data points vs amount of positive to negative text clasifications ##
        if nu_score > 0:
            negative_positive = 100 * float(nu_score) / float(v_total)
        else:
            negative_positive = 0.00
        if nd_score > 0:
            negative_negative = 100 * float(nd_score) / float(v_total)
        else:
            negative_negative = 0.00
        if pu_score > 0:
            positive_positive = 100 * float(pu_score) / float(v_total)
        else:
            positive_positive = 0.00
        if pd_score > 0:
            positive_negative = 100 * float(pd_score) / float(v_total)
        else:
            positive_negative = 0.00
            ## Calculation of total data points vs amount of positive to negative text clasifications ##
        overall_positive = 100 * float(ps_total) / float(total_data_points)
        overall_negative = 100 * float(ns_total) / float(total_data_points)
        with conn_refine.cursor() as cur:
            t_make = "CREATE TABLE IF NOT EXISTS " + self + " (time_stamp_now TIMESTAMP NULL" \
                                                              " DEFAULT CURRENT_TIMESTAMP," \
                                                              " id INT(30) NOT NULL AUTO_INCREMENT," \
                                                              " currency_name VARCHAR(255) NULL," \
                                                              " total_data_points INT(20) NULL," \
                                                              " positive_statement DECIMAL(20,10) NULL," \
                                                              " positive_opinions DECIMAL(20,10) NULL," \
                                                              " negative_statement DECIMAL(20,10) NULL," \
                                                              " negative_opinion DECIMAL(20,10) NULL," \
                                                              " overall_positive DECIMAL(20,10) NULL," \
                                                              " overall_negative DECIMAL(20,10) NULL," \
                                                              " negative_positive DECIMAL(20,10) NULL," \
                                                              " negative_negative DECIMAL(20,10) NULL," \
                                                              " positive_positive DECIMAL(20,10) NULL," \
                                                              " positive_negative DECIMAL(20,10) NULL," \
                                                              " polarity DECIMAL(4,2) NULL," \
                                                              " subjectivity DECIMAL(4,2) NULL," \
                                                              " PRIMARY KEY (id)) ENGINE = InnoDB" \
                                                              " DEFAULT CHARACTER SET = utf8mb4" \
                                                              " COLLATE = utf8mb4_unicode_ci"

            t_add = "INSERT INTO " + self + "(currency_name, total_data_points, negative_positive," \
                                              " negative_negative, positive_positive, positive_negative," \
                                              " positive_statement, positive_opinions, negative_statement," \
                                              " negative_opinion, overall_positive, overall_negative," \
                                              " polarity, subjectivity) VALUES (%s, %s, %s, %s, %s, %s," \
                                              " %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(t_make)
            cur.execute(t_add, (t_name, total_data_points, negative_positive,
                                negative_negative, positive_positive, positive_negative,
                                positive_statement, positive_opinions, negative_statement,
                                negative_opinion, overall_positive, overall_negative, f, b))
