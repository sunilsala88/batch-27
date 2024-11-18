import yfinance as yf
import mplfinance as mpf
import pandas_ta as ta
import numpy as np

data=yf.download(tickers='MSFT',start='2023-01-01',end='2023-12-30')
print(data)

doji=ta.cdl_pattern(data['Open'],data['High'],data['Low'],data['Close'],name="longline")
print(doji)
# doji.to_csv('sample.csv')
# print(doji[doji<0.0])
import numpy as np
data['doji']=doji.replace({100: 1,-100:1, 0: np.nan})
data['doji']=data['doji']*data['Close']
c=mpf.make_addplot(data['doji'],color='Black',type='scatter')
mpf.plot(data,addplot=c,type='candle',style='yahoo')
