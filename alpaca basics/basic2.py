
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.stock import StockHistoricalDataClient


from alpaca.data.requests import (
    StockBarsRequest,
)


api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"
data_api_url=None
symbol='GOOG'

# setup stock historical data client
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key, url_override = data_api_url)


# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/stockbars-1
now = datetime.now(ZoneInfo("America/New_York"))
req = StockBarsRequest(
    symbol_or_symbols = [symbol],
    timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Day), # specify timeframe
    start = now - timedelta(days = 300),                          # specify start datetime, default=the beginning of the current day.
    # end_date=None,                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
)
data=stock_historical_data_client.get_stock_bars(req).df
print(data)