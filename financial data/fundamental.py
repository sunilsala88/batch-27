import yfinance as yf

ticker_obj=yf.Ticker('RELIANCE.NS')
# d=ticker_obj.info
# print(d.keys())
# for i in d.keys():
#     print(i)

# print(d.get('beta'))

# df=ticker_obj.get_income_stmt()
# print(df)

d=ticker_obj.fast_info
print(d)