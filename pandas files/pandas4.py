
import pandas as pd

df=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/sp500.csv')
df.index.name='abc'
print(df)

# print(df['Price'][4])
# df.set_index('Name',inplace=True)
# print(df)

# #loc
# print(df.loc[ 'Accenture Plc', 'Price'])
# print(df.iloc[3,-2])

# df['new']=df['Price']+df['EPS']
# print(df)


df1=df['Price']
df2=df[['Sector','EPS']]
print(df1)
print(df2)


df3=pd.merge(df1,df2,on='abc')
print(df3)


data1=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/SBIN.csv')
data1.set_index('date',inplace=True)
data1=data1.iloc[:5]
data1=data1[['open','high']]
data1.index.name='c0'
print(data1)


data2=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/Unicorn_companies.csv')
data2=data2[['Company','Valuation']].iloc[:5]
data2.index=data1.index
data2.index.name='c0'
print(data2)

data3=pd.merge(data1,data2,on='c0')
print(data3)

l1=['a','b','c','d','e']
data3['new_col']=l1
print(data3)
print(data3['new_col'])



import numpy as np
df1=pd.DataFrame((np.arange(25).reshape(5,5)),columns=['c1','c2','c3','c4','c5'])
print(df1)

df2=pd.DataFrame((np.arange(25,50).reshape(5,5)),columns=['c1','c2','c3','c4','c5'])
print(df2)

df3=pd.concat([df1,df2])
df3.reset_index(inplace=True)
print(df3)





data1=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/SBIN.csv')
data1.set_index('date',inplace=True)
data1=data1.iloc[:5]
data1=data1[['open','high']]
# data1.index.name='c0'
print(data1)


data2=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/Unicorn_companies.csv')
data2=data2[['Company','Valuation']].iloc[:5]
data2.rename(columns={'Company':'open','Valuation':'high'},inplace=True)
# data2.index.name='c0'
print(data2)

data3=pd.concat([data1,data2])
print(data3)