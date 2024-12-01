#environment
#3.12.2
#pip install backtesting
#numpy pip install numpy==1.26.4
#bokeh pip install bokeh==2.4.3
#No module named 'pkg_resources' pip install setuptools
#yfinance pip install yfinance==0.2.37
from backtesting import Backtest, Strategy
import pandas_ta as ta
import yfinance as yf


class SmaCross(Strategy):
    n1 = 30
    n2 = 60

    def init(self):
        close = self.data['Adj Close'].s
        self.sma1 = self.I(ta.sma, close, self.n1)
        self.sma2 = self.I(ta.sma, close, self.n2)

    def next(self):

        if self.sma1[-1]>self.sma2[-1] and self.sma1[-2]<self.sma2[-2] :
            self.buy()
        elif self.sma1[-1]<self.sma2[-1] and self.sma1[-2]>self.sma2[-2]:
            self.sell()


data=yf.download('ADANIENT.NS',period='10y')
print(data)

bt = Backtest(data, SmaCross,
              cash=1_000, commission=.002,
              exclusive_orders=True)

output = bt.run()
print(output)
# bt.plot()
print(output['_trades'])