import time

start=time.time()

l=[1]*2+[0]*998
for x in [2,3,5,7,11,13,17,19,23,29,31]:
    for y in range(2,1000):
        if y%x==0:
            l[y]=1
    l[x]=0
l[2]=1
l[5]=1

d=9
while sum(l)!=999:
    for x in range(1,1000):
        if not l[x]:
            if d%x==0:
                l[x]=1
    d=d*10+9

for x in range(1000):
    if l[x]==0:
        S=x
        break

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
