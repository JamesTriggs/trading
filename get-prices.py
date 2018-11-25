from datetime import timedelta, datetime as dt
import pandas_datareader.data as web
from parse_file import parseFile

#get list of stocks from file
stock_list = 'ftse100.txt'
stocks = parseFile(stock_list)

#data gatherer
for stock in stocks:
    n = 100
    start = dt.datetime.now() - timedelta(days=n)
    end = dt.datetime.now()
    df = web.DataReader('{}'.format(stock), 'yahoo', start, end)
    df.to_csv('stocks/{}.csv'.format(stock))
