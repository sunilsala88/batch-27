
#v diff topic

def sample(a,b):
    print(a,b)
    sample(a,b)

sample(1,2)


def fun1(a,b):
    c=a+b
    return c

def fun2(t,p):
    b=fun1(t,p) #7
    return b-t #7-3

def fun3(o,p):
    a=fun1(o,p) #7
    b=fun2(o,p) #4
    return a+b #7+4

ans=fun3(3,4)
print(ans)