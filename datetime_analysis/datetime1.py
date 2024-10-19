# import datetime
import datetime as dt
# from datetime import datetime,timedelta
# from datetime import *

d1=dt.datetime(2024,10,13,10,30,30)
delta1=dt.timedelta(minutes=1)
print(d1)
print(d1+delta1)
ct=dt.datetime.now()
print(ct)

date1=dt.date(2024,12,12)
print(date1)

time1=dt.time(10,59,10)
print(time1)

def main():
    print('main')

# import time
# while True:
#     current=dt.datetime.now()
#     # print(current)
#     time.sleep(1)
#     if current.second in range(1,61,5):
#         main()
#         print(current)



#epoch to datetime
n=1738418781
dnew=dt.datetime.fromtimestamp(n)
print(dnew)

#datetime to epoch
d1=dt.datetime(2024,10,13,10,30,30)
print(d1)

n1=d1.timestamp()
print(n1)

#str to datetime
s1='2024-01-01 59-11-30'
format1='%Y-%m-%d %M-%H-%S'
n=dt.datetime.strptime(s1,format1)
print(n)

s2='24 September 2007'
format1='%d %B %Y'
n=dt.datetime.strptime(s2,format1)
print(n)
print(n.date())
print(n.time())

#datetime to str
d1=dt.datetime(2024,10,13,10,30,30)
print(d1)
format1='%d %B %Y'
s1=d1.strftime(format1)
print(s1)

a='55_30_11.2024.11.September'
#epoch time for this string
f2='%M_%S_%H.%Y.%d.%B'
a1=dt.datetime.strptime(a,f2)
print(a1.timestamp())