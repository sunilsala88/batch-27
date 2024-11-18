import pandas as pd

# df=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/Unicorn_companies.csv')
# print(df)

# # df=df.set_index('Company')
# df.set_index('Company',inplace=True)
# print(df)

# # df.set_index('Valuation',inplace=True,drop=True)
# # print(df)

# # print(df.reset_index(inplace=True))
# # print(df)

# # print(df['Year Founded']['SHEIN'])


# print(df.loc['Klarna','Continent'])
# print(df.iloc[4,-3])
# #get index of Klarna
# print(df.index.get_loc('Klarna'))
# print(df.loc['Zihaiguo','Date Joined'])
# print(df.iloc[-3,1])


# df1=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/sp500.csv')
# df1.set_index('Name',inplace=True)
# print(df1)

# print(df1.loc['Exelon Corp','EPS'])

# print(df1.index.get_loc('Exelon Corp'))
# print(df1.iloc[34,2])

# df2=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/stock_value.csv')

# df2.set_index('Date',inplace=True)
# print(df2)
# print(df2.loc['2020-01-02':'2020-01-08','tsla'])
# print(df2.iloc[0:5, -1])



# print(df)
# print(df.loc['Stripe':'Klarna' ,'Valuation':'Date Joined' ])
# print(df.loc[['Stripe','Klarna'] ,['Valuation','Date Joined'] ])

# print(df.iloc[ 3:5, 0:2])
# print(df.iloc[ [3,4], [0,1]])


# print(df.loc['Zihaiguo':'Zwift' ,'Year Founded':'Funding' ])
# print(df.loc[['Zihaiguo','Zopa','Zwift'] ,['Year Founded','Funding'] ])

# print(df.iloc[ -3:, -2:])
# print(df.iloc[ [-3,-2,-1], [-2,-1]])



df5=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/SBIN.csv')
print(df5)
df5.set_index('date', inplace=True)
print(df5)
d=df5.loc['2019-01-01 09:15:00':'2019-01-01 15:29:00','volume']
print(d)
print(d.sum()/d.shape[0])


