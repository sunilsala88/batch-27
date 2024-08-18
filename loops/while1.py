

# counter=1

# while True:
#     if counter==101:
#         break
#     if counter%2!=0:
#         print(counter)  
#     counter=counter+1



# stock_prices={'tsla':200,'goog':900,'nifty':890,'ongc':768}

# for i,j in stock_prices.items():
#     print(i,j)


# portfolio={}

# while True:
#     name=input('enter the name of stock(q to quit)')
#     if name.upper()=='Q':
#         break

#     found=stock_prices.get(name)
    
#     if found:
#         # portfolio.update({name:found})
#         portfolio[name]=found
    
#     else:
#         print('invalid input type again')

# print(portfolio)

#diff
#rev string
# st1='hello'
# lt1=[1,2,3]
# "olleh"
# 3,2,1

st1="hello"
l=len(st1)
# for i in range(l):
#     print(st1[i],end='')

#[0,1,2,3,4,5,6,7,8]

#[-1,-2,-3...-8]
#[8,7,6..0]

print(l)
#3 ways
print(list(range(l)))
print(list(range(-1,-l,-1)))
print(list(range(l-1,-1,-1)))

for i in range(-1,-l-1,-1):
    print(st1[i],end='')

print('\n')
for i in range(l-1,-1,-1):
    print(st1[i],end='')
print('\n')


st2='fessorpro'
l=len(st2)
i=0

while True:
    if i==l:
        break
    print(st2[i],end='')
    i=i+1
print('\n')



i=l-1
while True:
    if i==-1:
        break
    print(st2[i],end='')
    i=i-1
print('\n')


i=-1
while True:
    if i==-l-1:
        break
    print(st2[i],end='')
    i=i-1
print('\n')