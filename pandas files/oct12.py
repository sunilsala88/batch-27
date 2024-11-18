

import pandas as pd

data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')
# print(data)
df=data[1]

df.rename(columns={'Company name':"Company","Sector[12]":'Sector',"Date added[13]":"Date"},inplace=True)
# df.set_index('Company',inplace=True)
print(df)
a='Asian Paints'
print(a.replace(" ","-"))
# df['dash']= df['Company'].str.replace(" ","-").str.upper()
# print(df['Company'].str.upper())
print(df)

# a='2'
# i=int(a)
# print(df.info())

l1=[]
for data in df['Date']:
    print(data)
    if data[-3]=='[':
        l1.append(data[:-3])
    else:
        l1.append(data)
# 27 April 2012[a]
print(l1)
df['Date']=l1
print(df)
# l=[]
# for i in df['Company']:
#     l.append(i.replace(' ','-').upper())
# df['dash']=l
# print(df)

df['year']=df['Date'].str[-4:]
print(df)
print()
df['year']=df['year'].astype('int')
print(df.info())
print(df['year'].sum()/len(df['year']))
print(df['year'].mean())

df['year']=df['year'].astype('str')
print(df.info())