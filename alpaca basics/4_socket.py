import json
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import alpaca
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.crypto import CryptoHistoricalDataClient
from alpaca.trading.stream import TradingStream
from alpaca.data.live.crypto import CryptoDataStream

from alpaca.data.requests import (
    CryptoBarsRequest,
    CryptoQuoteRequest,
    CryptoTradesRequest,
    CryptoLatestQuoteRequest
    )
from alpaca.trading.requests import (
    GetAssetsRequest,
    MarketOrderRequest,
    LimitOrderRequest,
    StopLimitOrderRequest,
    GetOrdersRequest,
    ClosePositionRequest
)
from alpaca.trading.enums import (
    AssetClass,
    AssetStatus,
    OrderSide,
    OrderType,
    TimeInForce,
    QueryOrderStatus
)
from alpaca.common.exceptions import APIError

api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"

symbol="BTC/USD"




# subscribe trade updates
trade_stream_client = TradingStream(api_key, secret_key, paper='True', url_override = None)

async def trade_updates_handler(data):
    print(data)

trade_stream_client.subscribe_trade_updates(trade_updates_handler)
trade_stream_client.run()