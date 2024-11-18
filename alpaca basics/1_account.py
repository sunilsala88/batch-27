

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus

api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"
# paper=True enables paper trading
trading_client = TradingClient(api_key, secret_key, paper=True)


account = trading_client.get_account()

print(account)
print(account.equity)
# print(account.cash)
# print(type(account))


# pos=trading_client.get_all_positions()
# print(pos)

# import pandas as pd
# new_pos=[]
# for elem in pos:
#         new_pos.append(dict(elem))
# pos_df=pd.DataFrame(new_pos)
# print(pos_df)
# pos_df.to_csv('data.csv')








# # params to filter orders by
# request_params = GetOrdersRequest(
#                     status=QueryOrderStatus.OPEN,
#                     side=OrderSide.BUY
#                  )

# # orders that satisfy params
# orders = trading_client.get_orders(filter=request_params)
# print(orders)