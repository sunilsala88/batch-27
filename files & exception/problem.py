

stock_prices={'tsla':700,'goog':900,'amzn':690,'nifty':689}

def print_all_stocks():
    for i,j in stock_prices.items():
        print(i,j)
    
def input_stocks():
    portfolio={}
    while True:
        name=input('enter the stock name')
        if name.upper()=="Q":
            break
        found=stock_prices.get(name)
        if found:
            portfolio.update({name:found})
        else:
            print('unable to find the stock type again')
    return portfolio


def save_to_txt(porfolio):

    f=open('port.txt','w')

    for name,price in porfolio.items():
        v=name+":"+str(price)+'\n'
        f.write(v)
    f.close()


print_all_stocks()
p=input_stocks()
print(p)
save_to_txt(p)