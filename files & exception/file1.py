


#read some thing from file


#how to write into a file


# f=open('data1.txt','w')
# f.write('third line')
# f.close()


# f=open(r'/Users/algotrading2024/batch 27/files & exception/data3.txt','r')
# d=f.read()
# print(d)
# f.close()


f=open('/Users/algotrading2024/batch 27/files & exception/data3.txt','a')
f.write('third line')
f.close()


with open('datanew.txt','w') as f:
    f.write('new line')

