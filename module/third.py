x=100
y=200
number=200


#sel 4.1 get_name
#sel 5.1 getNameca

import yfinance as yf
data=yf.download('TSLA',period='1mo')
print(data)