

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