
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
data1=data1.iloc[:100]
data1=data1[['open','high']]
data1.index.name='c0'
print(data1)


data2=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/Unicorn_companies.csv')
data2=data2[['Company','Valuation']].iloc[:100]
data2.index=data1.index
data2.index.name='c0'
print(data2)

data3=pd.merge(data1,data2,on='c0')
print(data3)

