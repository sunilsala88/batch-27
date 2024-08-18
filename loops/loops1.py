
list1=['goog','amzn','tsla']


# #type 1
#to go through each elem of list
for i in list1:
    print(i)

#type 2
#to repeat a code for n number of time
for i in range(100):
    print('hello')


#print all number from 1 to 100
number=0
for i in range(100):
    number=number+1
    print(number)
    
for  i in range(100):
    print(i)

#type 3
#to go through each elem of list by using index (range function)

for i in range(len(list1)):
    print(list1[i])
    # print(i)


name=['tsla','goog','nifty']
prices=[55,77,88]

stock_prices={}

for i in range(len(name)):
    stock_prices.update({name[i]:prices[i]})
    print(name[i],prices[i])

print(stock_prices)


#first 10 fib numbers

number1=0
number2=1

for i in range(8):
    print(number1,number2)
    number3=number1+number2
    print(number3)
    number1=number2
    number2=number3

#type 4
#used on a dictionary
stock_prices={'tsla':700,'ongc':900,'hdfc':970}

print(list(stock_prices.keys()))

print(list(stock_prices.values()))

print(list(stock_prices.items()))
s=[]
p=[]

for k,v in stock_prices.items():
    print(k,v)
    s.append(k)
    p.append(v)
print(s)
print(p)


