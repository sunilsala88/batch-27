# # import pandas as pd
# # d=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
# # # print(d)
# # df=d[1]
# # # print(df)
# # # print(list(df.columns))
# # df.drop('Notes',axis=1,inplace=True)
# # print(df)
# # # print(df.info())

# # # df.set_index('Company',inplace=True)
# # print(df)
# # # df.drop(28,axis=0,inplace=True)
# # # print(df.index.to_list())
# # # df.to_csv('dow.csv')
# # print(df[(df['Exchange']=='NASDAQ') & (df['Industry']=='Information technology')]['Company'].to_list())


import pandas as pd
df=pd.read_csv('dow.csv')
print(df)

# # print(df.isna())
# # print(df.notna())
# # df.dropna(axis=1,inplace=True)
# # print(df)

# # df['Industry'].fillna('IT',inplace=True)
# # df['Exchange'].fillna('NSE',inplace=True)
# # print(df)

# # df['Industry'].fillna(method='ffill', inplace=True)
# # print(df)

# a=df[df['Industry']=='Information technology'].index.to_list()
# print(a)
# df.drop(a,axis=0,inplace=True)
# print(df)



s='3.45%'
print(float(s[:-1]))

df['weigh']=df['Index weighting'].str.replace('%',"")
df['float_weigh']=df['weigh'].astype("float")
print(df)
print(df.info())

