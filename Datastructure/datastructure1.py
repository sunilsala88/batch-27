

#list

a=[1,2,3,'amzn','goog','tsla']
print(a)

#indexing
# print(a[6])

#slicing
print(a[3:-1])

#slicing formula
# var_name[start:end+1]
# 5=end_ind+1
# end_ind=5-1=4

#get a list excluding first and last element

a='fessor'
b=['f','e','s','s','o','r']

#indexing and slicing is same
b.append('p')
print(b)

b.insert(0,'hello')

# b[1]='o'
print(b)

a=a.replace('e','o')
print(a)



string1='adfladknf'

# string1=string1.upper()
print(string1)

s=string1.index('n')
print(s)

print(string1.count('a'))

list1=[4,5,6,7,6,6]
list1.append(8)
print(list1)

i=list1.index(5)
print(i)
print(list1.count(6))
list1.insert(1,'hello')
print(list1)


stocks=['TSLA',"GOOG","AMZN",88]

# stocks.clear()
# stocks.extend(list1)

# r=stocks.pop(-1)
# print(r)

del stocks[-1]

print(stocks)
# stocks.remove('GOOG')
stocks.reverse()
print(stocks)



#tuple
#round bracket
#immutable

a=(1,2,3,1)
c=a.index(3)
print(c)

