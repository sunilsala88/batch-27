#yfinance pip install yfinance==0.2.37
import yfinance as yf
data=yf.download('ADANIENT.NS',period='10y')

print(data.info())

# c=[]
# for i in data.columns:
#     c.append(i[0])
# data.columns=c

print(data)