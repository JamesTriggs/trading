from datetime import timedelta
import datetime as dt
import pandas_datareader.data as web
from parse_file import parseFile

#get list of stocks from file
stock_list = 'ftse100.txt'
stocks = parseFile(stock_list)

def main():
    gatherData()

#data gatherer
def gatherData():
    for stock in stocks:
        n = 100
        start = dt.datetime.now() - timedelta(days=n)
        end = dt.datetime.now()
        df = web.DataReader('{}'.format(stock), 'yahoo', start, end)
        df.to_csv('stocks/{}.csv'.format(stock))

if __name__ == '__main__':
    main()