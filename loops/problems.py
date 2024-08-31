
#fibonacci series

prev2=0
prev1=1

# for i in range(8):
#     curr=prev2+prev1
#     print(curr)
#     prev2=prev1
#     prev1=curr
fib=[0,1]
counter=1
while True:

    curr=prev2+prev1
    # print(curr)
    fib.append(curr)
    prev2=prev1
    prev1=curr

    if counter==9:
        break
    counter=counter+1

    # counter=counter+1
print(fib)



#largest number
list1= [2000, 3000, 1500, 4000, 2800]
high=list1[0]

# for i in list1:
#     if i>high:
#         high=i

# print(high)


i=0
while True:
    if i==len(list1):
        break
    if list1[i]>high:
        high=list1[i]
    i=i+1
print(high)


prices=[100, 105, 110]
Volumes=[200, 150, 300]
vwap=[]
# for i in range(len(prices)):
#     v=prices[i] * Volumes[i]
#     vwap.append(v)
# print(vwap)


i=0
while True:

    if i==len(prices):
        break


    v=(prices[i] * Volumes[i])
    vwap.append(v)

    i=i+1

print(vwap)
print(sum(vwap)/sum(Volumes))



prices=[100, 120, 130, 140, 150]
avg=sum(prices)/len(prices)

count=0
for p in prices:
    if p>avg:
        count=count+1

print(count)

i=0
count=0
while True:
    if i==len(prices):
        break
    if prices[i]>avg:
        # count=count+1
        count+=1
    i=i+1

print(count)

#palindrome

st1='racecar'
new=''
for i in range(-1,-len(st1)-1,-1):
    new=new+st1[i]
print(new)
if st1==new:
    print('palindrome')
else:
    print('not a palindrome')



list3=[3, 1, 4, 1, 5, 9,55,67,3,5,77,44,67]

high=list3[0]
high2=list3[0]
for i in list3:
    if i>high:
        high2=high
        high=i

print(high,high2)


iv=1000
i=0.08
# fv=2000
year=0
cv=iv
while True:
    if cv>iv*2:
        break
    cv=cv+cv*i
    print(cv)
    year=year+1
print(year)


count=0
interest=0.08
sum=1000
end=sum*2
while sum <end:
    profit=sum*interest
    sum=sum+profit
    count=count+1
print (count)