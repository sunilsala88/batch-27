import yfinance as yf
import pandas_ta as ta

tickers=['^NSEI','TSLA','AMZN']
for t in tickers:
    data=yf.download(tickers=t,period='6mo',interval='1d')
    d=ta.sma(data['Close'],10)
    print(d)

    d1=ta.ema(data['Close'],10)
    print(d1.iloc[-1])

#ModuleNotFoundError: No module named 'pkg_resources'

# ImportError: cannot import name 'NaN' from 'numpy' (/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/numpy/__init__.py). Did you mean: 'nan'?


#pip install numpy==1.26.4