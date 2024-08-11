




stocks={
    'BANK':[{'HDFC':300},{'KOTAK':800}],
    "TECH":[{'TSLA':890},{'TCS':950}]
}

# index_stock={'HDFC':0,'KOTAK':1,'TSLA':0,'TCS':1}

name='TCS'
print(stocks.get('TECH')[1].get(name))


