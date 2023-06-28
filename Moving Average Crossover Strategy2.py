#!/usr/bin/env python
# coding: utf-8

# In[218]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
import seaborn as sns 
from datetime import datetime, timedelta
import time

#start_time = time.time()

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
unrealizedpnl = []
prices = []

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
    prices.append(stock['SMA50'][date])


profit_per_trade = pd.Series(pnl)
profit_per_trade.index = exit_date

#unrealised pnl
unrlzd = np.cumsum(np.multiply(np.diff(prices), numberoftrades[1:]))
unrlzdpnl = pd.DataFrame(unrlzd)     #converted to dataframe for plotting 
unrlzdpnl = unrlzdS.set_index(stock.index[:-1])


#plotting
plt.plot(np.cumsum(profit_per_trade),'-o')
plt.plot(unrlzdpnl, '--', label='Unrealized PnL')
plt.legend()
plt.xlabel('date')
plt.ylabel('Realized PnL')
plt.show()

#end_time = time.time()
#execution_time = end_time - start_time
#print("Execution Time: {:.2f} seconds".format(execution_time))



#separate plot of realized and unrealized pnl
fig, ax1 = plt.subplots(figsize=(25, 12))
ax2 = ax1.twinx()

ax1.plot(np.cumsum(profit_per_trade),'-o', color='blue', lw=4)
ax2.plot(stock.index[:-1], unrlzd, color='green', lw=4)

ax1.set_xlabel("Date")
ax1.set_ylabel("Realized PnL", color='blue', fontsize=14)
ax1.tick_params(axis="y")

ax2.set_ylabel("Unrealized PnL", color='green', fontsize=14)
ax2.tick_params(axis="y")

fig.suptitle("Moving Average Crossover Strategy", fontsize=30)
fig.autofmt_xdate()
plt.grid()




#numerical realized and unrealized pnl
final_unrlzd = unrlzd[-1]
print(final_unrlzd, sum(profit_per_trade))




#Realized Percentage PnL
rlzd = profit_per_trade.pct_change()
rlzd_cum = (rlzd + 1).cumprod()
plt.grid()
plt.xlabel('Date')
plt.ylabel('Percentage PnL')
rlzd_cum.plot()
plt.title('Realized Percentage PnL')
plt.grid()
plt.show()


# In[ ]:




