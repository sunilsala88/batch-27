# import yfinance as yf

# df=yf.download(tickers='BTC-USD',period='2y',interval='1h')
# df.reset_index(inplace=True)
# print(df)
# print(df.info())
#1m 7 days
#5m 90 days
#1h 700 days
#daily no limit

#alpaca

#accessor 

import pandas as pd
data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')
df1=data[1]
# print(df1)
df1.rename(columns={'Company name':'Company',"Sector[12]":'Sector',"Date added[13]":"Date"},inplace=True)
df1.set_index('Symbol',inplace=True)

s='hello world'
print(s.replace(' ','-'))

#str accessor
df1['Sector']= df1['Sector'].str.replace(" ","-")


l1=[]
for d in df1['Date']:
    if d[-3]=='[':
        l1.append(d[:-3])
    else:
        l1.append(d)
df1['Date']=l1
print(df1)
#dt accessor
d1=pd.to_timedelta(1,unit='day')

df1['Date']=pd.to_datetime(df1['Date'],format='%d %B %Y')
print(df1)

df1['Date']=df1['Date']+d1


df1['y']=df1['Date'].dt.day
print(df1)
print(df1.info())
