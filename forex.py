"""Script to gather forex currency details and perform statistical analysis."""
import sys
import psycopg2
import datetime
import threading
from forex_python.converter import CurrencyRates
from config import config

curr_list = 'currencies.txt'

def main():
    """Main entry point for the script."""
    runLoop()
    # t = threading.Timer
    # t.daemon = True
    # t.start()
    # t(5.0, runLoop)
    # print('loop passed')

def runLoop():
    conn = connect()
    currencies = parseFile(curr_list)
    currency_rate = getCurrencyPairPrice(currencies)
    commitPricesToDb(currency_rate, conn, curr_list)

def parseFile(curr_list):
    """Open text file of currencies and compile into list object""" 
    with open(curr_list) as f:
        currencies = f.read().splitlines()
    return currencies

def connect():
    """Connect to Postgresql database"""
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

def getCurrencyPairPrice(currencies):
    """Get the current exchange rate of each currency pair"""
    currency_rate = []
    c = CurrencyRates()
    for item in currencies:
        stringboi = str(item)
        rate = c.get_rate('GBP', stringboi)
        currency_row = ['GBP', item, datetime.datetime.now(), rate]
        currency_rate.append(currency_row)

    return currency_rate

def commitPricesToDb(currency_rate, conn, curr_list):
    """Take list of currency pair prices and commit to Db"""
    cur = conn.cursor()
    for currency in currency_rate:
        #try:
        statement = ("""INSERT INTO forex.{} (date_taken, rate) VALUES ('{}', '{}')""".format(currency[1], currency[2], currency[3]))
        print(statement)
        cur.execute(statement)
        #except:
            #print("I can't do that for some reason, would be great if i told you why wouldn't it?")
    conn.commit()

if __name__ == '__main__':
    sys.exit(main())
