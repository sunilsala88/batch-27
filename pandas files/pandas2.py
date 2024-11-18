import pandas as pd

data=pd.read_csv('/Users/algotrading2024/batch 27/pandas files/sp500.csv')
print(data)

print(list(data.columns))
print(list(data.index))

print(data.sort_values(['Price'],ascending=False))

#more than 1 column Dataframe
#single column is called Series

# #approach 1
print(data['Sector'])

# #approach 2
print(data.Sector)

print(data[ ['Name','Price','EPS' ]])
print(data['Price'])
print(data['Price']>90)
print(data[data['Price']>90])