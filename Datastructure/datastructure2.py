
#dictionary
#mutable
stock_prices={"amzn":100,'tsla':200,'goog':600}

print(stock_prices['tsla'])


print(stock_prices.get('nifty'))

# a='hello'
# print(a[9])


a=[1,2,3]
print(a.append(5))
print(a)


var1=[33,44,55]

# print(var1[0])

var1[0]=100
print(var1)




#read
print(stock_prices['amzn'])
print(stock_prices.get('amzn'))

#update
# stock_prices['amzn']=200
stock_prices.update({'amzn':200})
print(stock_prices)

#create/write
# stock_prices.update({'nifty':800})
stock_prices['nifty']=800
print(stock_prices)

#delet
# stock_prices.pop('tsla')
del stock_prices['tsla']
print(stock_prices)


a=[11,22,33]
stock_prices




s1={1,2,3,1,2,2,2,2}
s1.remove(2)
s1.add(6)
a=s1.pop()
print(a)
print(s1)

print(list(s1))