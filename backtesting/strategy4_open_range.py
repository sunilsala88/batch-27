
from backtesting import Backtest, Strategy

import pandas as pd
import yfinance as yf
import time



class ORBStrategy(Strategy):
    
    def init(self):
        self.orb_high = None
        self.orb_low = None
        self.trade=0


    def next(self):
            if self.data.index[-1].time() == pd.Timestamp('10:00').time():
                df=self.data.df
                d=self.data.index[-1]
                d=pd.to_datetime(d.date())
                df=df[df.index>=d]
                self.orb_high = df.High.max()
                self.orb_low = df.Low.min()
                self.trade=0
                # print(self.orb_high, self.orb_low)

        
            if not self.position and self.orb_high and self.orb_low:
                # print('inside condition')
                if (self.data.Close[-1] > self.orb_high) and self.trade==0:
                    # print('buy condition satisfied')
                    p=self.data.Close[-1]
                    self.buy(sl=self.data.Close[-1]*0.97,tp=self.data.Close[-1]*1.03)
                    self.trade=1
                elif (self.data.Close[-1] < self.orb_low) and self.trade==0:
                    # print('sell condition satisfied')
                    self.sell(sl=self.data.Close[-1]*1.03,tp=self.data.Close[-1]*0.97)
                    self.trade=1
            elif self.position:
                # Close position by the end of the day
                # print('i have some position')
                if self.data.index[-1].time() == pd.Timestamp('15:20').time():
                    self.position.close()
                # print(self.position)



# import yfinance as yf
# data=yf.download('AMZN',start='2024-11-20',end='2024-12-07',interval='5m')

data=pd.read_csv('/Users/algotrading2024/batch 27/backtesting/data.csv')
print(data)
data.drop(['symbol','trade_count','vwap','volume'],axis=1,inplace=True)
data.rename(columns={'timestamp':'Date','open':'Open','high':'High','low':'Low','close':'Close'},inplace=True)
data['Date']=pd.to_datetime(data['Date'])
data['Date']=data['Date'].dt.tz_convert('US/Eastern')
data['Date']=data['Date'].dt.tz_localize(None)
data.set_index('Date',inplace=True)
data=data.between_time('09:00:00', '16:00:00')
print(data)
data=data.iloc[:5000,]

# data.reset_index(inplace=True)
# data['Datetime']=data['Datetime'].dt.tz_localize(None)
# data.set_index('Datetime',inplace=True)

# print(data)
bt = Backtest(data, ORBStrategy, cash=300, commission=.002)
stats = bt.run()
print(stats)
bt.plot()



# data = fetch_data('AMZN')
# print(data)


  # Focus on regular trading hours
# data.to_csv('data.csv')
# data['Date']=data['Date'].dt.tz_localize(None)
# data.set_index('Date',inplace=True)
# data = data.between_time('09:00:00', '16:00:00')

# bt = Backtest(data, ORBStrategy, cash=100_000, commission=.002)
# stats = bt.run()
# print(stats)
# bt.plot()

# results = {}
# for stock in stocks:
#     data = fetch_data(stock)
#     print(data)
#     data['Date']=data['Date'].dt.tz_localize(None)
#     data.set_index('Date',inplace=True)
#     bt = Backtest(data, ORBStrategy, cash=100_000, commission=.002)
#     stats = bt.run()
#     results[stock] = stats
#     bt.plot()

# for stock, stats in results.items():
#     print(f"{stock}:")
#     print(stats)