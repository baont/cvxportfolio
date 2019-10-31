import os
import sys
import matplotlib
sys.path.insert(0, os.path.abspath('..'))

import numpy as np
import pandas as pd
import quandl

quandl.ApiConfig.api_key = 'hJshhxzE_HoL6VKHNVcd'

import cvxportfolio as cp

print("hello world")

tickers = ['AMZN', 'GOOGL', 'TSLA', 'NKE']
start_date='2012-01-01'
end_date='2016-12-31'
returns = pd.DataFrame(dict([(ticker, quandl.get('WIKI/'+ticker,
                                    start_date=start_date,
                                    end_date=end_date)['Adj. Close'].pct_change())
                for ticker in tickers]))
returns[["USDOLLAR"]]=quandl.get('FRED/DTB3', start_date=start_date, end_date=end_date)/(250*100)
returns = returns.fillna(method='ffill').iloc[1:]

returns.tail()