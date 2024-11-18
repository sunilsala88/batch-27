import yfinance as yf
import mplfinance as mpf
import pandas_ta as ta
import numpy as np

data=yf.download(tickers='MSFT',start='2022-01-01',end='2024-01-01')
print(data)

# c=ta.cagr(data['Close'])
# print(c)


# def CAGR(DF):
#     "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
#     df = DF.copy()
#     df["return"] = DF["Close"].pct_change()
#     print(df)
#     df["cum_return"] = (1 + df["return"]).cumprod()
#     n = len(df)/252
#     CAGR = (df["cum_return"].iloc[-1])**(1/n) - 1
#     return CAGR

# c2=CAGR(data)
# print(c2)


d=ta.max_drawdown(data['Close'],method='percent')
print(d)

mpf.plot(data,type='candle',style='yahoo')

ta.calmar_ratio()
ta.sharpe_ratio()
ta.sortino_ratio()


a='hello'
a.find()
a.replace()
a.count()
