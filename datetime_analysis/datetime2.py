import pandas as pd


df=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/SBIN.csv')
print(df)
print(df.info())
df['date']=pd.to_datetime(df['date'])
print(df)
print(df.info())




import pandas as pd

data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')
# print(data)
df=data[1]

df.rename(columns={'Company name':"Company","Sector[12]":'Sector',"Date added[13]":"Date"},inplace=True)
print(df)
a=[]
for i in df['Date']:
    if i[-3]=='[':
        a.append(i[:-3])
    else:
        a.append(i)
df['Date']=a
print(df)
df['Date']=pd.to_datetime(df['Date'],format='%d %B %Y')
print(df)
print(df.info())

single_date=pd.to_datetime('2020-01-01')
print(df[df['Date']>single_date])

td1=pd.to_timedelta(1,unit='D')
df['Date']=df['Date']+td1
print(df)
print('df')