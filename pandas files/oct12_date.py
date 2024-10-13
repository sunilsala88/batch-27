import datetime
# import datetime as dt
# from datetime import datetime

for i in range(1,32):
    d=datetime.datetime(2024,10,i,11,11,22)
    if d.weekday()==3:
        print(d)

def demo1():
    print('started')

import time
while True:
    demo1()
    time.sleep(5)
    print(datetime.datetime.now())

current_time=datetime.datetime.now()
print(current_time.second)