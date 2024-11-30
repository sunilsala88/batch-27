import random
import time
import datetime
import pandas as pd
import pandas_ta as ta
#getting all active orders
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
import pandas as pd
api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"
trading_client = TradingClient(api_key, secret_key, paper=True)


from alpaca.data.historical import CryptoHistoricalDataClient
# setup crypto historical data client
crypto_historical_data_client = CryptoHistoricalDataClient()
from zoneinfo import ZoneInfo
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


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
    data['sma_50']=ta.sma(data['close'],50)
    data['sma_20']=ta.sma(data['close'],20)
    return data

def close_this_position(ticker_name):
    try:
        position = trading_client.get_open_position(ticker_name)
        print(position)
        c=trading_client.close_position(ticker_name)
        print(c)
        print('position closed')
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

def strategy(hist_df,ticker):
    print('inside strategy conditional code ')
    # print(hist_df)
    print(ticker)
    buy_condition=(hist_df['sma_20'].iloc[-1]>hist_df['sma_50'].iloc[-1]) and (hist_df['sma_20'].iloc[-2]<hist_df['sma_50'].iloc[-2])
    money=float(trading_client.get_account().cash)
    money=money/3
    print(money)
    closing_price=hist_df['close'].iloc[-1]
    if money>closing_price:
        if buy_condition:
            print('buy condition satisfied')
            trade_buy_stocks(ticker,closing_price)
        else:
            print('no condition satisfied')
    else:
        print('we dont have enough money to trade')

def main_strategy_code():
    pos_df=get_all_position()
    ord_df=get_all_open_orders()
    print(pos_df)
    print(ord_df)
    print('we are inside main strategy code it should run every 1 min')
    for ticker in tickers:
        print(ticker)
        #fetch historical data and indicators
        hist_df=get_historical_crypto_data(ticker,1,10)
        print(hist_df)

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
            strategy(hist_df,ticker)

        elif len(pos_df)!=0 and ticker.replace('/','') not in pos_df['symbol'].to_list():
            print('we have some position but ticker is not in pos')
            strategy(hist_df,ticker)

        elif len(pos_df)!=0 and ticker.replace('/','')  in pos_df['symbol'].to_list():
            print('we have some pos and ticker is in pos')
            curr_quant=float(pos_df[pos_df['symbol']==ticker.replace('/','')]['qty'].iloc[-1])
            print(curr_quant)

            if curr_quant==0:
                print('my quantity is 0')
                strategy(hist_df,ticker)
            elif curr_quant>0:
                print('we are already long')
                sell_condition=(hist_df['sma_20'].iloc[-1]<hist_df['sma_50'].iloc[-1]) and (hist_df['sma_20'].iloc[-2]>hist_df['sma_50'].iloc[-2])
                if sell_condition:
                    print('sell condition is satisfied ')
                    close_this_position(ticker.replace('/',''))
                else:
                    print('sell condition not satisfied')

current_time=datetime.datetime.now()
print(current_time)

start_hour,start_min=16,48
end_hour,end_min=17,50

start_time=datetime.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min)
end_time=datetime.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min)

print(start_time)
print(end_time)

while datetime.datetime.now()<start_time:
    print(datetime.datetime.now())
    time.sleep(1)
print('we have reached start time')



while True:
    if datetime.datetime.now()>end_time:
        break
    ct=datetime.datetime.now()

    print(ct)
    if ct.second==1: #and ct.minute in range(0,60,5):#[0,5,10,15..55]
        main_strategy_code()
    time.sleep(1)
print('strategy stopped')