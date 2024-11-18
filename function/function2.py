


def avg1(lnum):
    global b
    total=0
    b=20
    print(b)
    
    for i in lnum:
        total=total+i
    ans=total/len(lnum)
    return ans

b=10
n=[1,2,3,45,6,45,6,34]
a=avg1(n)
print(a)

print(b)