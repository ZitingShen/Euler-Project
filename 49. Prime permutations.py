import time

start=time.time()

l=[1,0]*5000
l[1],l[2]=1,0
v=3
while v<10000:
    if not l[v]:
        i=v*3
        while i<10000:
            l[i]=1
            i+=2*v
    v+=2

for x in range(1000,10000):
    S="148748178147"
    if not l[x]:
        for y in range(x+1,(10000+x)//2):
            if not l[y]:
                if not l[2*y-x]:
                    if "".join(sorted(str(y)))=="".join(sorted(str(x))):
                        if "".join(sorted(str(2*y-x)))=="".join(sorted(str(x))):
                           S=str(x)+str(y)+str(2*y-x)
                           break
        if S!="148748178147":
            break

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
