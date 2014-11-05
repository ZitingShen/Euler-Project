import time
import math

start=time.time()

abundant=[]
for x in range(12,28124):
    pd=1
    for y in range(2,math.ceil(x**0.5)):
        if x%y==0:
            pd+=y
            pd+=x//y
    if x%(x**0.5)==0:
        pd+=int(x**0.5)
    if pd>x:
        abundant.append(x)

numbers=[0]*28123
for x in range(len(abundant)):
    for y in range(x,len(abundant)):
        if abundant[x]+abundant[y]<28123:
            numbers[abundant[x]+abundant[y]]=1

S=0
for x in range(28123):
    if numbers[x]==0:
        S+=x

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
