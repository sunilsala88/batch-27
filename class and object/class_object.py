

#what is class
#class is a blueprint of object

#what is object
#object is an instance of class

#what is class attribute (characteristics,properties)
#they are variable inside a class ascessible to everyone


#what is instance/object attribute (characteristics,properties)
#they are variable only availabe to object

#what is method
#any function created inside a class is called method

#constructor
#its a first function executed when you create a object

#dunder method

#prosedural programming
#step by step programming

#oops (object oriented programming)
#class and object

class Car:
    wheels=4
    material='metal'

    #create a contructor
    def __init__(self,name,color,fuel,price):
        print('i am a constructor')
        self.name=name
        self.color=color
        self.fuel=fuel
        self.price=price
    
    def __str__(self):
        return self.fuel
    
  


# c1=Car(name='tata',color='red',fuel='petrol',price=300000)
# c2=Car('bmw','black','ev',3000000)
# print(c2.price)
# print(c1.price)
# print(c1)




class BankAccount:

    def __init__(self,account_number : str,balance:int):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance= self.balance+amount
        else:
            print('invalid amount')

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print('invalid amount')

    def get_balance(self):
        return self.balance


# Create a new bank account instance
my_account = BankAccount("12345678", 1000)

# Deposit and withdraw
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.get_balance())  # Output: 1300




class Broker:
    stock_prices={
        'tsla':1000,
        'nifty':800,
        'reliance':1500,
        'tata':2000,
        'goog':2500,
    }
    def __init__(self, name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.wallet=balance
        self.portfolio={}

    def buy(self,stock_name):
        found=self.stock_prices.get(stock_name)
        if found:
            if self.wallet> found:
                self.portfolio.update({stock_name:found})
                self.wallet=self.wallet-found
            else:
                print('you dont have enough money to buy the stock')
        else:
            print('stock doesnt exist')

    def sell(self,stock_name):
        found=self.portfolio.get(stock_name)
        if found:  
            self.portfolio.pop(stock_name)
            self.wallet=self.wallet+found
        else:
            print('stock doesnt exist in the portfolio')

    def get_portfolio(self):
        return self.portfolio

user1=Broker('niraj',2345,2000)

user1.buy('tsla')
print(user1.get_portfolio())

user1.buy('nifty')
print(user1.get_portfolio())

user1.buy('tata')
print(user1.get_portfolio())


user1.sell('nifty')
print(user1.get_portfolio())



#about self
#1 any instance attribute created inside a class is created using self
#2 all methods will have self as first argument
#3 all class and instance attribute can only be accessed using self




class BankAccount:
    def __init__(self,account_number : str,balance:int):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance= self.balance+amount
        else:
            print('invalid amount')

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print('invalid amount')

    def get_balance(self):
        return self.balance
    
acc1=BankAccount('1234',500)
b=acc1.get_balance()
c=BankAccount.get_balance(acc1)
print(b,c)


acc2=BankAccount('1234',1000)
b=acc2.get_balance()
c=BankAccount.get_balance(acc2)
print(b,c)