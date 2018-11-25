import datetime as dt
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
from parse_file import parseFile

#simple chart for adj close
#df['Adj Close'].plot()
#plt.show()

# 100 day moving average
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#resampling data to blocks of days 
#df_ohlc = df['Adj Close'].resample('10D').ohlc()
#df_volume = df['Volume'].resample('10D').sum()

#dunno
#df_ohlc.reset_index(inplace=True)
#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())

#draw graph dimensions
#ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

#place data on axis
#ax1.plot(df.index, df['Adj Close'])
#ax1.plot(df.index, df['100ma'])
#ax2.bar(df.index, df['Volume'])

#show graph
#plt.show()