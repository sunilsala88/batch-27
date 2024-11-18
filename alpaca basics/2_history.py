from alpaca.data.historical import StockHistoricalDataClient
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo

from alpaca.data.requests import StockBarsRequest ,StockTradesRequest,StockQuotesRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

from alpaca.data.enums import Adjustment

api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"

# setup stock historical data client
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key)

symbol='GOOG'

# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/stockbars-1
now = datetime.now(ZoneInfo("America/New_York"))


req = StockBarsRequest(
    symbol_or_symbols = symbol,
    timeframe=TimeFrame(amount = 5, unit = TimeFrameUnit.Minute), # specify timeframe
    start = now - timedelta(days = 100),                          # specify start datetime, default=the beginning of the current day.
    # end_date=None,                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
)
data=stock_historical_data_client.get_stock_bars(req).df
print(data)



# now = datetime.now(ZoneInfo("America/New_York"))
# req = StockBarsRequest(
#     symbol_or_symbols = symbol,
#     timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Day), # specify timeframe
#     start = now - timedelta(days = 3),                       # specify start datetime, default=the beginning of the current day.
    
#     # end_date=datetime(2024,7,24),                                        # specify end datetime, default=now
#     # limit = 2,                                               # specify limit
#     adjustment=Adjustment.ALL
# )
# data=stock_historical_data_client.get_stock_bars(req).df
# print(data)



# get historical trades by symbol
# req = StockTradesRequest(
#     symbol_or_symbols = symbol,
#     start = now - timedelta(days = 2),                          # specify start datetime, default=the beginning of the current day.
#     # end=None,                                             # specify end datetime, default=now
#     # limit = 2,                                                # specify limit
# )
# data=stock_historical_data_client.get_stock_trades(req).df
# print(data)


# get historical quotes by symbol
req = StockQuotesRequest(
    symbol_or_symbols = [symbol],
    start = now - timedelta(days = 3),                      # specify start datetime, default=the beginning of the current day.
    # end=None,                                             # specify end datetime, default=now
    # limit = 2,                                              # specify limit
)
data=stock_historical_data_client.get_stock_quotes(req).df
print(data)