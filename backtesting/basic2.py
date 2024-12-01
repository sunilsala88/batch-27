from backtesting import Backtest,Strategy
import pandas_ta as ta
import yfinance as yf
import pandas as pd
import time

def get_sma(close_price,length):
    d=ta.sma(close=close_price,length=length)
    return d

class sma_cross(Strategy):
    n1=9
    n2=3

    def init(self):
        print('inside init')
        n_data=self.data.df
        print(n_data)
        self.sma1=self.I(get_sma,n_data['Close'],self.n1)
        self.sma2=self.I(get_sma,n_data['Close'],self.n2)
        print(self.sma1)
        print(self.sma2)
    

    def next(self):
        # print(self.data.df)
        # print(self.sma1[-1],self,self.sma2[-1],self.sma1[-2],self,self.sma2[-2])
        # print(self.data.Close[-1],self.data.Close[-2])
        if (self.sma1[-1]>self.sma2[-1] ) and (self.sma1[-2]<self.sma2[-2] ):
            print(self.data.index[-1])
            print('buy cond satisfied')
            print(self.sma1[-1],self.sma2[-1],self.sma1[-2],self.sma2[-2]  )
            if self.position.is_short:
                self.position.close()
                print('closing short position')
            self.buy()

        elif (self.sma1[-1]<self.sma2[-1] ) and (self.sma1[-2]>self.sma2[-2] ):
            print(self.data.index[-1])
            print('sell cond satisfied')
            print(self.sma1[-1],self.sma2[-1],self.sma1[-2],self.sma2[-2]  )
            if self.position.is_long:
                self.position.close()
                print('closing long position')
            self.sell()
        
        print(self.position)
        time.sleep(1)
         


data=yf.download('GOOG',period='10y')
print(data)
sma=get_sma(data['Close'],90)
print(sma)

# data=pd.read_csv('/Users/algotrading2024/batch 27/data.csv')
# print(data)

bt=Backtest(data,sma_cross,cash=5_000,commission=0.02)
output=bt.run()
print(output)
bt.plot()