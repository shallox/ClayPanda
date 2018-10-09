# ClayPanda
Data collection and analysis for reddit/bittrex.

Things you will need to have set up.
  MySQL server.
  Python 3.4 or higher.
  
  Python Packages:
    Textblob
    Bittrex api
    Praw

To run for the 1st time, set up a database for both Reddit and Bittrex data.
Configure the settings.py.example.py file with the correct reddit/bittrex api access info
and then rename it to settings.py.
When run for the 1st time, the script will create the tables it needs and populate the data,
the 1st run will take some time because it is populating the DB with 3 or so months worth of bittrex data.
When run every hour after that however it will collect only whats missing.
