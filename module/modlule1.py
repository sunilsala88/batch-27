
#module,package,library

#pypi.org

import random
import time
import sys

for i in range(10):
    r=random.randint(10,100)
    print(r)
    time.sleep(1)
    if r>80:
        print('exiting')
        sys.exit()


print('last line')

import os
p=os.getcwd()
print(p)