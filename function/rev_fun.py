
def calc_avg(list2):
    total=0
    for elem in list2:
        total=total+elem

    avg=total/len(list2)

    return avg


list1=[33,44,5,6,7]
a=calc_avg(list1)
print(a)


def power(b,p):
    return b**p,b,p

a=power(3,2)[0]
print(a)

#positional keyword argument
#positional will come before keyword argument
#default argument
#default argument always comes at the end in func defination

def place_order(name : str,price,side,order_type='MKT',quant =1 ):
    """
    #doc string
    this is a simple order function
    allowed parameter for order type is "MKT","LMT","STP"
    o is not allowed for side only 1(long) and -1 (short) is allowed
    """
    if side>0:
        print(f"buying {order_type} order {name} quantity {quant} at price {price} ")
    else:
        print(f"selling {order_type} order {name} quantity {quant} at price {price} ")        

place_order('goog',400,-1)
place_order(order_type='limit',price=500,quant=50,side=-1,name='tsla')
place_order('reliance',8,1)



def fun1(a,b,c,d):
    return a+b+c+d

a=fun1(*[3,4,5,4])
print(a)


# *args
def fun2(*name):
    print(name)

fun2('tsla','goog',55,66,77,'ajsdfj')


# *kwargs

def fun3(**stock_prices):
    print(stock_prices)

fun3(tsla=300,goog=800)


