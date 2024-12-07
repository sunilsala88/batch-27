import yfinance as yf

data=yf.download(tickers='^NSEI',period='6mo',interval='1d')
print(data)

# import datetime as dt
# start1=dt.datetime(2024,1,1,0,0,0,0)

# data_1m=yf.download('TSLA',start=start1,end='2024-10-19',interval='1m')
# print(data_1m)
# data.to_csv('data.csv')

# ohlcv_dict = {
#  'Open': 'first',
#  'High': 'max',
#  'Low': 'min',
#  'Close': 'last',
#  'Volume': 'sum'
# }

# new_data=data_1m.resample('60min').agg(ohlcv_dict)
# print(new_data.head(15))
# new_data.dropna(inplace=True)
# print(new_data) 

#matplotlib
#mplfinance

# import mplfinance as mpf
# mpf.plot(data,type='candle',style='yahoo')