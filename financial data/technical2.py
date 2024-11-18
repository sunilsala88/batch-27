import yfinance as yf
import pandas_ta as ta


data=yf.download(tickers='TSLA',period='6mo',interval='1d')
# d=ta.sma(data['Close'],10)
# print(d)

# atr=ta.atr(data['High'],data['Low'],data['Close'],15)
# print(atr)

atr=data.ta.atr(15)
print(atr)

#adx
#supertrend


sd1=ta.supertrend(data['High'],data['Low'],data['Close'],length=12,multiplier=5)
print(sd1)

#bollinger bands

macd=ta.macd(data['Close'])
print(macd)

bb=ta.bbands(data['Close'])
print(bb)