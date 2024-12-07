import pandas_ta as ta
import pandas as pd
from backtesting import Strategy, Backtest

def supertrend1(high_data,low_data,close_data,n1):
    o=ta.supertrend(high_data,low_data,close_data,length=n1)
    print(o)
    return o[f'SUPERTd_{n1}_3.0']
def supertrend2(high_data,low_data,close_data,n1):
    o=ta.supertrend(high_data,low_data,close_data,length=n1)
    return o[f'SUPERT_{n1}_3.0']


class supertrend(Strategy):
    n1=10

    def init(self):
        self.super1=self.I(supertrend1,self.data.High.s,self.data.Low.s,self.data.Close.s,self.n1)
        self.super2=self.I(supertrend2,self.data.High.s,self.data.Low.s,self.data.Close.s,self.n1)

    def next(self):
        # pass
        if self.super1[-1]>0 and self.super1[-2]<0:
            if self.position.is_short:
                self.position.close()

            self.buy()
        elif self.super1[-1]<0 and self.super1[-2]>0:
            if self.position.is_long:
                self.position.close()
            else:
                pass
            self.sell()



# import yfinance as yf
# data=yf.download('AMZN',start='2020-05-24',end='2024-06-29',interval='1D')
# print(data)

data=pd.read_csv('/Users/algotrading2024/batch 27/backtesting/SPY.csv')
print(data)
data.drop(['symbol','trade_count','vwap','volume'],axis=1,inplace=True)
data.rename(columns={'timestamp':'Date','open':'Open','high':'High','low':'Low','close':'Close'},inplace=True)
data['Date']=pd.to_datetime(data['Date'])
data.set_index('Date',inplace=True)
print(data)
data=data.iloc[:10000,]


# print(supertrend1(data['High'], data['Low'], data['Close']))
# print(supertrend2(data['High'], data['Low'], data['Close']))

bt=Backtest(data,supertrend,cash=500)
output=bt.run()
print(output)
bt.plot()
print(output['_trades'])


a=range(10,100,5)
stats=bt.optimize(n1=a,maximize='Return [%]')
print(stats)
print(stats['_strategy'])
# bt.plot()
