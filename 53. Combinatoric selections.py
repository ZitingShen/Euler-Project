import time
from functools import reduce

start=time.time()

S=0
for x in range(23,101):
    for y in range(1,x+1):
        v=1
        for a in range(x-y+1,x+1):
            v*=a
        for b in range(1,y+1):
            v/=b
        if v>1000000:
            S+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
