import time
from math import ceil

start=time.time()

def nway(total,coins):
    if len(coins)==1:
        return 1
    else:
        c,coins=coins[0],coins[1:]
        S=0
        if total%c==0:
            S+=1
        for x in range(ceil(total/c)):
                S+=nway(total-x*c,coins)
        return S

S=nway(200,(200,100,50,20,10,5,2,1))

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
