#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
import seaborn as sns 
from datetime import datetime, timedelta


stock = yf.download(tickers='AAPL', period='20y')


#create simple moving averages for 50-day and 200-day periods of AAPL

stock['SMA200'] = stock['Adj Close'].rolling(200).mean()

stock['SMA50'] = stock['Adj Close'].rolling(50).mean()

stock = stock.dropna()

stock.tail()

stock.plot(y=["Adj Close", "SMA200","SMA50"], kind="line", figsize=(20, 12))

#Trading Strategy
inpos = 0
pnl = []
numberoftrades = []
time_in_trade = []
exit_date = []

for date in stock.index:
    
    if stock['SMA50'][date] < stock['SMA200'][date] and not inpos:
        'Enter Short Position'
        entry = stock['SMA50'][date]
        open_time = date
        inpos = -1
        
    elif stock['SMA50'][date] > stock['SMA200'][date] and inpos ==-1:
        'Exit Short Position'
        p =  entry - stock['SMA50'][date]
        pnl.append(p)
        inpos = 0
        time_in_trade.append((date-open_time).days)
        exit_date.append(date)
        print('Exit Short:',sum(pnl))
        
    elif stock['SMA50'][date] > stock['SMA200'][date] and not inpos:
        'Enter Long Position'
        entry = stock['SMA50'][date]
        open_time = date
        inpos = 1
        
    elif stock['SMA50'][date] < stock['SMA200'][date] and inpos == 1:
        'Exit Long Position'
        p = stock['SMA50'][date] - entry
        pnl.append(p)
        inpos = 0
        time_in_trade.append((date-open_time).days)
        exit_date.append(date)
        print('Exit Long:',sum(pnl))
    numberoftrades.append(inpos)


profit_per_trade = pd.Series(pnl)
profit_per_trade.index = exit_date

plt.plot(np.cumsum(profit_per_trade),'-o')
plt.xlabel('date')
plt.ylabel('Realized PnL')
plt.show()


# In[ ]:




