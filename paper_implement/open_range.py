import random
import time
import datetime
import pendulum as pdt
import pandas as pd
import pandas_ta as ta
#getting all active orders
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
import pandas as pd
api_key='PKB872RM09BHVAMWPS9P'
secret_key='yFTUvVwM5f9G0mrZJWFIZkZu5eF4mxbAq5b4wAFy'
trading_client = TradingClient(api_key, secret_key, paper=True)


from alpaca.data.historical import CryptoHistoricalDataClient
# setup crypto historical data client
crypto_historical_data_client = CryptoHistoricalDataClient()
from zoneinfo import ZoneInfo
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

import logging
logging.basicConfig(level=logging.INFO, filename=f'open_range_{datetime.date.today()}',filemode='w',format="%(asctime)s - %(message)s")

try:
    order_filled_dataframe=pd.read_csv('order_filled_list.csv')
    order_filled_dataframe.set_index('time',inplace=True)

except:
    column_names = ['time','ticker','price','action']
    order_filled_dataframe = pd.DataFrame(columns=column_names)
    order_filled_dataframe.set_index('time',inplace=True)


tickers=["BTC/USD","ETH/USD"]


def get_all_open_orders():
    # params to filter orders by
    request_params = GetOrdersRequest(
                        status=QueryOrderStatus.OPEN
                    )

    # orders that satisfy params
    orders = trading_client.get_orders(filter=request_params)
    new_order=[]
    for elem in orders:
        new_order.append(dict(elem))

    order_df=pd.DataFrame(new_order)
    return order_df

def get_all_position():

    pos=trading_client.get_all_positions()


    new_pos=[]
    for elem in pos:
        new_pos.append(dict(elem))

    pos_df=pd.DataFrame(new_pos)
    # pos_df.to_csv('pos.csv')
    return pos_df


def get_historical_crypto_data(ticker_name,time_frame,days):

    now = datetime.datetime.now(ZoneInfo("America/New_York"))
    req = CryptoBarsRequest(
        symbol_or_symbols = ticker_name,
        timeframe=TimeFrame(amount = time_frame, unit = TimeFrameUnit.Minute), # specify timeframe
        start = now - datetime.timedelta(days = days),                          # specify start datetime, default=the beginning of the current day.
        # end_date=None,                                        # specify end datetime, default=now
        # limit = 2,                                               # specify limit
    )
    data=crypto_historical_data_client.get_crypto_bars(req).df
    data['sma_10']=ta.sma(data['close'],10)
    data['sma_30']=ta.sma(data['close'],30)
    return data

def close_this_position(ticker_name):
    try:
        position = trading_client.get_open_position(ticker_name)
        print(position)
        c=trading_client.close_position(ticker_name)
        print(c)
        print('position closed')
        a=[ticker_name,closing_price,'SELL']
        order_filled_dataframe.loc[pdt.now('UTC')] = a
        order_filled_dataframe.to_csv('order_filled_list.csv')
    except:
        print('position does not exist')

def trade_buy_stocks(ticker,closing_price):
    print('placing market order')
    # preparing orders
    market_order_data = MarketOrderRequest(
                        symbol=ticker,
                        qty=1,
                        side=OrderSide.BUY,
                        time_in_force=TimeInForce.GTC
                        )

    # Market order
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )
    a=[ticker,closing_price,'BUY']
    order_filled_dataframe.loc[pdt.now('UTC')] = a
    order_filled_dataframe.to_csv('order_filled_list.csv')
    

def trade_sell_stocks(ticker,closing_price):
    print('placing market order')
    # preparing orders
    market_order_data = MarketOrderRequest(
                        symbol=ticker,
                        qty=1,
                        side=OrderSide.SELL,
                        time_in_force=TimeInForce.GTC
                        )

    # Market order
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )
    a=[ticker,closing_price,'SELL']
    order_filled_dataframe.loc[pdt.now('UTC')] = a
    order_filled_dataframe.to_csv('order_filled_list.csv')

def strategy(hist_df,ticker,high_level,low_level):
    print('inside strategy conditional code ')
    # print(hist_df)
    print(ticker)
    buy_condition=hist_df['close'].iloc[-1]>high_level
    # sell_condition=hist_df['close'].iloc[-1]<low_level
    money=float(trading_client.get_account().cash)
    money=money/3
    print(money)
    closing_price=hist_df['close'].iloc[-1]
    if money>closing_price:
        if buy_condition:
            print('buy condition satisfied')
            trade_buy_stocks(ticker,closing_price)
        # elif sell_condition:
        #     print('sell condition satisfied')
        #     trade_sell_stocks(ticker, closing_price)
        else:
            print('no condition satisfied')
    else:
        print('we dont have enough money to trade')

def get_level(hist_df):
    # ct=datetime.datetime.now()
    # start_range=datetime.datetime(ct.year, ct.month, ct.day, 19, 0)
    # end_range=datetime.datetime(ct.year, ct.month, ct.day, 20, 0)
    ct = pdt.now('UTC')
    start_range=pdt.datetime(ct.year, ct.month, ct.day, 0, 0,tz='UTC')
    end_range=pdt.datetime(ct.year, ct.month, ct.day, 2, 0,tz='UTC')
    print(start_range, end_range)
    hist_df.reset_index(inplace=True)
    print(hist_df)
    # hist_df['date']=hist_df['date'].dt.tz_localize(None)
    hist_df.set_index('timestamp',inplace=True)
    print(hist_df.index)
    print(start_range, end_range)


    hist_df=hist_df[start_range:end_range]
    print(hist_df)
    high_level=hist_df.high.max()
    low_level=hist_df.low.min()
    return high_level,low_level


def main_strategy_code():
    pos_df=get_all_position()
    ord_df=get_all_open_orders()
    print(pos_df)
    pos_df.to_csv('pos.csv')
    print(ord_df)
    for ticker in tickers:
        print(ticker)
        #fetch historical data and indicators
        hist_df=get_historical_crypto_data(ticker,1,10)
        print(hist_df)

        high_level,low_level=get_level(hist_df)
        print(high_level, low_level)

        money=float(trading_client.get_account().cash)
        money=money/3
        print(money)
        ltp=hist_df['close'].iloc[-1]
        print(ltp)
        quantity=money/ltp
        print(quantity)

        if quantity<1:
            continue
        
        if pos_df.empty:
            print('we dont have any position')
            strategy(hist_df,ticker,high_level,low_level)

        elif len(pos_df)!=0 and ticker.replace('/','') not in pos_df['symbol'].to_list():
            print('we have some position but ticker is not in pos')
            strategy(hist_df,ticker,high_level,low_level)

        # elif len(pos_df)!=0 and ticker.replace('/','')  in pos_df['symbol'].to_list():
        #     print('we have some pos and ticker is in pos')
        #     curr_quant=float(pos_df[pos_df['symbol']==ticker.replace('/','')]['qty'].iloc[-1])
        #     print(curr_quant)
        #     if curr_quant==0:
        #         print('my quantity is 0')
        #         strategy(hist_df,ticker)
        #     elif curr_quant>0:
        #         print('we are already long')
        #         sell_condition=(hist_df['sma_10'].iloc[-1]<hist_df['sma_30'].iloc[-1]) and (hist_df['sma_10'].iloc[-2]>hist_df['sma_30'].iloc[-2])
        #         if sell_condition:
        #             print('sell condition is satisfied ')
        #             close_this_position(ticker.replace('/',''))
        #         else:
        #             print('sell condition not satisfied')
            
        if pdt.now('UTC').hour>=23 and pdt.now('UTC').minute>=58:
            close_this_position(ticker)

current_time=datetime.datetime.now()
print(current_time)

start_hour,start_min=14,45
end_hour,end_min=15,58

start_time=datetime.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min)
end_time=datetime.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min)

print(start_time)
print(end_time)

while datetime.datetime.now()<start_time:
    print(datetime.datetime.now())
    time.sleep(1)

candle_size=60

while True:
    if datetime.datetime.now()>end_time:
        break
    print(datetime.datetime.now())
    print('before run')
    main_strategy_code()
    print('after run')
    seconds_till_next_min= candle_size- datetime.datetime.now().second
    print('sleeping for',seconds_till_next_min)
    time.sleep(seconds_till_next_min)

print('strategy stopped')


