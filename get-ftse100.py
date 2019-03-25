import bs4 as bs
import datetime as dt 
import os
import pandas_datareader.data as web 
import pickle
import requests

def save_ftse100_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/FTSE_100_Index')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    with open("ftse100tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    
    return tickers

def get_data_from_yahoo(reload_ftse100=True):
    
    if reload_ftse100:
        tickers = save_ftse100_tickers()
    else:
        with open("ftse100tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    start = dt.datetime(2010,1, 1)
    end = dt.datetime.now()
    #This bit needs the new data gather method that is in the to-do list
    for ticker in tickers:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'morningstar', start, end)
            df.reset_index(inplace=True)
            df.set_index("Date", inplace=True)
            df = df.drop("Symbol", axis=1)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()