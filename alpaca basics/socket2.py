from alpaca.data.live import StockDataStream,CryptoDataStream

import credentials as cs

api_key = cs.api_key
secret_key = cs.secret_key

symbol="BTC/USD"

wss_client = CryptoDataStream(api_key,secret_key)

# async handler
async def quote_data_handler(data):
    # quote data will arrive here
    print("$$$$$$$$",data.symbol,data.timestamp,data.ask_price)

wss_client.subscribe_quotes(quote_data_handler, symbol)
wss_client.subscribe_quotes(quote_data_handler, 'ETH/USD')

wss_client.run()


# ython" "/Users/algotrading2024/alpaca 2024/realtimesocket.py"
# symbol='BTC/USD' timestamp=datetime.datetime(2024, 6, 9, 14, 27, 24, 628504, tzinfo=datetime.timezone.utc) ask_exchange=None ask_price=69441.5 ask_size=0.279387 bid_exchange=None bid_price=69370.0 bid_size=0.5607 conditions=None tape=None
# symbol='BTC/USD' timestamp=datetime.datetime(2024, 6, 9, 14, 27, 24, 628928, tzinfo=datetime.timezone.utc) ask_exchange=None ask_price=69475.0 ask_size=0.8266 bid_exchange=None bid_price=69370.0 bid_size=0.5607 conditions=None tape=None
# symbol='BTC/USD' timestamp=datetime.datetime(2024, 6, 9, 14, 27, 24, 629010, tzinfo=datetime.timezone.utc) ask_exchange=None ask_price=69412.437 ask_size=0.27654 bid_exchange=None bid_price=69370.0 bid_size=0.5607 conditions=None tape=None
# symbol='BTC/USD' timestamp=datetime.datetime(2024, 6, 9, 14, 27, 24, 629016, tzinfo=datetime.timezone.utc) ask_exchange=None ask_price=69412.437 ask_size=0.27654 bid_exchange=None bid_price=69338.353 bid_size=0.82515 conditions=None tape=None
# symbol='BTC/USD' timestamp=datetime.datetime(2024, 6, 9, 14, 27, 24, 629245, tzinfo=datetime.timezone.utc) ask_exchange=None ask_price=69412.437 ask_size=0.27654 bid_exchange=None bid_price=69334.7 bid_size=0.2803 conditions=None tape=None