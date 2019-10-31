import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import numpy as np
import pandas as pd
import quandl

import cvxportfolio as cp

tickers = ['AMZN', 'GOOGL', 'MCD', 'NKE']
start_date='2016-01-01'
end_date=pd.datetime.today().date()
prices = pd.DataFrame(dict([(ticker, quandl.get('WIKI/'+ticker,
                                    start_date=start_date,
                                    end_date=end_date)['Adj. Close'])
                for ticker in tickers]))

returns=prices.pct_change()
returns[["USDOLLAR"]]=quandl.get('FRED/DTB3', start_date=start_date, end_date=end_date)/(250*100)
returns = returns.fillna(method='ffill').iloc[1:]

r_hat = returns.rolling(window=250, min_periods=250).mean().shift(1).dropna()
Sigma_hat = returns.rolling(window=250, min_periods=250).cov().dropna()

tcost_model=cp.TcostModel(half_spread=10E-4)
hcost_model=cp.HcostModel(borrow_costs=1E-4)

risk_model = cp.FullSigma(Sigma_hat)
gamma_risk, gamma_trade, gamma_hold = 5., 1., 1.
leverage_limit = cp.LeverageLimit(3)

spo_policy = cp.SinglePeriodOpt(return_forecast=r_hat,
                                costs=[gamma_risk*risk_model, gamma_trade*tcost_model, gamma_hold*hcost_model],
                                constraints=[leverage_limit])

current_portfolio=pd.Series(index=r_hat.columns,data=0)
current_portfolio.USDOLLAR=10000

t=pd.to_datetime('2017-01-01', infer_datetime_format=True);
# t = pd.datetime.today()
shares_to_trade=spo_policy.get_rounded_trades(current_portfolio, prices, t)
print(shares_to_trade)

pd.DataFrame({pd.datetime.today().date().__str__():shares_to_trade}).to_excel('shares_to_trade.xls')