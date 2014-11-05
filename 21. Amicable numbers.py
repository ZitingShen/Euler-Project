import time
import math
 
start = time.time()

def proper_divisor(num):
    pd=1
    for x in range(2,math.ceil(num**0.5)):
        if num%x==0:
            pd+=x
            pd+=num//x
    if num%(num**0.5)==0:
        pd+=int(num**0.5)
    return pd

S=0
l=[1]*2+[0]*9997
for x in range(1,10000):
    if not l[x-1]:
        y=proper_divisor(x)
        if y<10000 and x!=y and x==proper_divisor(y):
            print(x,y)
            S+=x+y
            l[x-1]=1
            l[y-1]=1

elapsed = (time.time() - start)
print("found %s in %s seconds" % (S,elapsed))
