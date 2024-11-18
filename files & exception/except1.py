
# try:
#     num1=int(input('enter number 1'))
#     num2=int(input('enter number 2'))
#     ans=num1/num2
#     print(ans)
# except:
#     print('input is incorrect')

# print('imp info :have a great day')





# try:
#     num1=int(input('enter number 1'))
#     num2=int(input('enter number 2'))
#     ans=num1/num2
#     print(ans)
# except Exception as e:
#     print(e)
#     print('input is incorrect')
# print('imp info :have a great day')

# num1=int(input('enter number 1'))
# num2=int(input('enter number 2'))
# ans=num1/num2
# print(ans)

#ZeroDivisionError
#ValueError:



try:
    num1=int(input('enter number 1'))
    num2=int(input('enter number 2'))
    ans=num1/num2
    print(ans)
except ZeroDivisionError:
    print('zero is not allowed for num2')
except ValueError:
    print('alphabets are not allowed as a number')

print('imp info :have a great day')
