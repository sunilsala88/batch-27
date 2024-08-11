

list1=[4,5,1,2]

#type 1
for item in list1:
    if item%2!=0:
        print(item, ' is odd')


# string1='hello'

# for char in string1:
#     print(char)

total=0
for a in list1:
    total=total+a
print(total)

#type 2
# print(list(range(10)))
# print(list(range(10,20)))
# print(list(range(10,50,5)))