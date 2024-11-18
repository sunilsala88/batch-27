import yfinance as yf
import mplfinance as mpf
import pandas_ta as ta
import numpy as np

data=yf.download(tickers='MSFT',start='2023-01-01',end='2023-12-30')
print(data)

data['sma']=ta.sma(data['Close'],20)
data['ema']=ta.ema(data['Close'],10)

print(data)

# a=mpf.make_addplot(data['sma'],color='Blue')
# b=mpf.make_addplot(data['ema'],color='Black')

# mpf.plot(data,addplot=[a,b],type='candle',style='yahoo')

bands=ta.bbands(data['Close'],10)
print(bands)

data['upper']=bands['BBU_10_2.0']
data['lower']=bands['BBL_10_2.0']
data['middle']=bands['BBM_10_2.0']
print(data)


# a=mpf.make_addplot(data['upper'],color='Blue')
# b=mpf.make_addplot(data['lower'],color='Black')
# c=mpf.make_addplot(data['middle'],color='Yellow')
# mpf.plot(data,addplot=[a,b,c],type='candle',style='yahoo')


sp1=ta.supertrend(data['High'],data['Low'],data['Close'])
print(sp1)

# c=mpf.make_addplot(sp1['SUPERT_7_3.0'],color='Black')
# mpf.plot(data,addplot=c,type='candle',style='yahoo')

macd=ta.macd(data['Close'])
print(macd)



# a=mpf.make_addplot(macd['MACD_12_26_9'],color='Blue',panel=1)
# b=mpf.make_addplot(macd['MACDh_12_26_9'],color='Black',panel=1,type='bar')
# c=mpf.make_addplot(macd['MACDs_12_26_9'],color='Yellow',panel=1)
# mpf.plot(data,addplot=[a,b,c],type='candle',style='yahoo')

atr=ta.atr(data['High'],data['Low'],data['Close'])
adx=ta.adx(data['High'],data['Low'],data['Close'])
rsi=ta.rsi(data['Close'])

print(atr)
print(adx)
print(rsi)

# a=mpf.make_addplot(atr,color='Blue',panel=1)
# b=mpf.make_addplot(adx['ADX_14'],color='Black',panel=1)
# c=mpf.make_addplot(rsi,color='Yellow',panel=1)
# mpf.plot(data,addplot=[a,b,c],type='candle',style='yahoo')


doji=ta.cdl_pattern(data['Open'],data['High'],data['Low'],data['Close'],name="longline")
print(doji)
import numpy as np
data['doji']=doji.replace({100: 1, 0: np.nan})
data['doji']=data['doji']*data['Close']
c=mpf.make_addplot(data['doji'],color='Black',type='scatter')
mpf.plot(data,addplot=c,type='candle',style='yahoo')



# inside=ta.cdl_inside(data['Open'],data['High'],data['Low'],data['Close'])
# print(inside)


# data['inside']=inside.replace({-1:1, 0: np.nan})
# data['inside']=data['inside']*data['Close']
# c=mpf.make_addplot(data['inside'],color='Black',type='scatter')
# mpf.plot(data,addplot=c,type='candle',style='yahoo')

# start=ta.sho