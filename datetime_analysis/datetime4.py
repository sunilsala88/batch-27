import yfinance as yf

df=yf.download(tickers='TSLA',period='2y',interval='1h')
df.reset_index(inplace=True)
print(df)

df['time']=df['Datetime'].dt.time
# print(df.to_string())

# import datetime as dt
# s=dt.datetime.now()
# print(s)
# print(s.time())

# l1=[]
# for d in df['Datetime']:
#     l1.append(d.time())
# df['time']=l1
# print(df)
import pandas as pd
d1=pd.to_timedelta(30,unit='m')
print(d1)
df['Datetime']=df['Datetime']-d1
print(df)
print(df.info())