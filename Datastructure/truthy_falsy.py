
#falsy value
#0
#Flase
#""
#[]
#{}
#()
#None

#truthy value
#all other are truthy value


stock_prices={'tsla':500,'goog':900,'amzn':600}
stock_name='tsla'
found=stock_prices.get(stock_name)
if found:
    print(found)
else:
    print('not found')