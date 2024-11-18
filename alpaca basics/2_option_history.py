from alpaca.data.historical.option import OptionHistoricalDataClient
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo

from alpaca.data.requests import OptionBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

from alpaca.trading.requests import GetOptionContractsRequest

from alpaca.data.enums import Adjustment
from alpaca.trading.enums import AssetStatus

from alpaca.trading.client import TradingClient

api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"


# symbol='SPY'

# get list of options contracts for the given underlying symbol (e.g. SPY,AAPL)
# - get_option_contracts() is a new method to get list of options contracts
# - in this example, we get 2 options contracts for SPY,AAPL
# - you can continue to fetch options contracts by specifying page_token from next_page_token of response
# underlying_symbols = ['SPY']
# req = GetOptionContractsRequest(
#     underlying_symbols = underlying_symbols,               # specify underlying symbols
#     status = AssetStatus.ACTIVE,                           # specify asset status: active (default)
#     expiration_date = None,                                # specify expiration date (specified date + 1 day range)
#     expiration_date_gte = None,                            # we can pass date object
#     expiration_date_lte = None,                            # or string (YYYY-MM-DD)
#     root_symbol = None,                                    # specify root symbol
#     type = None,                                           # specify option type (ContractType.CALL or ContractType.PUT)
#     style = None,                                          # specify option style (ContractStyle.AMERICAN or ContractStyle.EUROPEAN)
#     strike_price_gte = None,                               # specify strike price range
#     strike_price_lte = None,                               # specify strike price range
#     limit = None,                                             # specify limit
#     page_token = None,                                     # specify page token
# )
# # setup clients
# trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=True)
# res = trade_client.get_option_contracts(req)
# print(res)


symbol="SPY241118C00579000"

option_historical_data_client = OptionHistoricalDataClient(api_key, secret_key)
now = datetime.now(ZoneInfo("America/New_York"))
# get options historical bars by symbol
req = OptionBarsRequest(
    symbol_or_symbols = symbol,
    timeframe = TimeFrame(amount = 1, unit = TimeFrameUnit.Hour),   # specify timeframe
    start = now - timedelta(days = 5),                              # specify start datetime, default=the beginning of the current day.
    # end_date=None,                                                # specify end datetime, default=now
    # limit = 2,                                                      # specify limit
)
data=option_historical_data_client.get_option_bars(req).df


print(data)