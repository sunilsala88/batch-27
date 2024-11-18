

import pandas as pd

#csv

df1=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/sp500.csv')
print(df1)

#list of dict

# l1=[{'a':100,'b':200},{'a':500,'b':900}]
# df2=pd.DataFrame(l1,index=[77,88])
# print(df2)

# #dict of list
# d3={
#     'x':[11,22,33],
#     'y':[44,55,66],
#     'z':[77,88,99]
# }
# df3=pd.DataFrame(d3)
# print(df3)

#list of list
l2=[[11,22,33],[44,55,66],[77,88,99]]
df4=pd.DataFrame(l2,index=['x','y','z'],columns=['c1','c2','c3'])
print(df4)

# #dataframe from numpy array
# import numpy as np
# arr1=np.arange(100).reshape(10,10)
# print(arr1)
# df5=pd.DataFrame(arr1)
# print(df5)

df=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/SBIN.csv')
print(df)
print(df.info())