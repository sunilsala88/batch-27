

#square of a number
def square1(number):
    ans=number**2
    return ans


number=2
# ans=number**2
# print(ans)
a=square1(number)
print(a)

#avg of list of numbers

def avg1(lnum):
    total=0
    for i in lnum:
        total=total+i
    ans=total/len(lnum)
    return ans

n=[1,2,3,45,6,45,6,34]
a=avg1(n)
print(a)

def is_even_odd(num):
    if num%2!=1:
        a='even'
    else:
        a='odd'
    return a

ans=is_even_odd(10)
print(ans)




#fibonacci series
def fibonacci(n):
    prev2=0
    prev1=1
    fib=[0,1]
    counter=1
    while True:
        curr=prev2+prev1
        if counter==n-1:
            break
        fib.append(curr)
        prev2=prev1
        prev1=curr

        counter=counter+1
    return fib

a=fibonacci(10)
print(a)


def is_palindrome(st1):
   
    new=''
    for i in range(-1,-len(st1)-1,-1):
        new=new+st1[i]
    print(new)
    if st1==new:
        return True
    else:
        return False

if is_palindrome('ttuttr'):
    print('its a palindrome')
else:
    print('its not a palindrome')



def calc_power(num1:int,num2:int):
    ans=num1**num2
    print(ans)
    

calc_power(2,3)


def abs():
    print('hello')
    return [1,2,3]
    

r=abs()
print(r)




# def maximum(list1:list):
#     max=list1[0]
#     for elem in list1:
#         if elem>max:
#             max=elem
    
#     return max

# m=maximum([4,5,6,7])
# print(m)

# def area(radius:float|int):
#     return (radius**2)*3.14

# ans=area('asdf')
# print(ans)







