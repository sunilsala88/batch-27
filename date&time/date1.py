import datetime
# import datetime as dt

d1=datetime.datetime(2024,8,14,17,56,10)
print(d1)

delta1=datetime.timedelta(days=30)
print(d1-delta1)

print(datetime.datetime.now())

import time
while True:
    if datetime.datetime.now().minute==4:
        break
    print(datetime.datetime.now())
    time.sleep(1)
