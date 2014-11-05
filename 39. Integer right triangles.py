import time

start=time.time()

l=[0]*1001
for x in range(1,16):
    s=4*x**2+6*x+2
    i=1
    while i*s<1001:
        l[i*s]+=1
        i+=1

for x in range(2,12):
    s=8*x**2+4*x
    i=1
    while i*s<1001:
        l[i*s]+=1
        i+=1

num=0
for x in range(1001):
    if l[x]>num:
        num=l[x]
        S=x

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
