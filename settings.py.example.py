from bittrex.bittrex import Bittrex, API_V2_0, API_V1_1
import praw
import pymysql

## Settings ##

## Bittrex ##
brex = Bittrex(api_key="put_api_key_here", api_secret='put_api_secret_here',
                       api_version=API_V1_1)
## Reddit ##
reddit = praw.Reddit(client_id='put_reddit_api_id_here',
                     client_secret='put_reddit_secret_here',
                     user_agent='Bot name here',
                     username='reddit user name here',
                     password='account password here')

## MySql ##
conn = pymysql.connect(host='database server name',
                         user='user account',
                         password='password',
                         db='database name',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)