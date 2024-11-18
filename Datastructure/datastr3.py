


# a=(1,2,3)
# a1=a[0]
# a2=a[1]
# a3=a[2]
# print(a1,a2,a3)
# a1,a2,a3=[66,77,88]
# print(a1,a2,a3)


#type cast
# int str float
# list dict 

# d1=(44,55)
# d=list(d1)
# print(d)


# s1='hello'
# #immutable
# #indexing
# #slicing
# #find index

# #join split strip
# print('   asdfkjasf'.strip())

# a=['i','j','k']
# print('+'.join(a))

# word='1bc-asdfkj-akdfj-akldfj'
# print(word.split('a'))

# #list
# list1=[55,66,77]
# l2=['a','b','c']

# #add value
# list1.append(99)
# print(list1)

# list1.extend(l2)
# print(list1)

# list1.insert(0,'hello')
# print(list1)

# #del value
# list1.pop(-1) 
# print(list1)

# list1.remove('hello')
# print(list1)

# #update
# list1[-1]='z'
# print(list1)

# #access indexing 
# print(list1[0])

# #slicing
# print(list1[-3:])

# #replace value in list
# i=list1.index('a')
# list1[i]='i'
# print(list1)


#dictionary

d1={'amzn':400,'tsla':900,'nifty':6000,'ongc':7000}

#no index in dictonary no indexing no slicing

#get value using index
print(d1['tsla'])
print(d1.get('tsla'))

#add a new key value pair
# d1['goog']=600
d1.update({'goog':600})


#updat 
# d1['tsla']=1000
d1.update({'tsla':1000})
print(d1)


#del
# del d1['amzn']
d1.pop('amzn')
print(d1)

#functions used in loops
print(d1.keys())
print(d1.values())
print(d1.items())



#list of dict
ld1= [
    {'a':11,'b':44},
    {5:66,'x':'z'},
    
]
print(ld1[1].get('x'))

#dict of list
dl1={
    'tech':['GOOG','TSLA','AMZN'],
    'bank':['ICICI','HDFC','JPMORGAN']
}
print(dl1.get('bank')[1].lower())

#list of list

ll1=[ [44,55,66] , [77,88,89] , [3,2,5] ]

print(ll1[1][1])
#dict of dict

dd1={'k1':{6:88},'k2':{8:99}}
print(dd1.get('k2').get(8))