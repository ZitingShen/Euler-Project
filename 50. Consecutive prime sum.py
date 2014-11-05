import time

start=time.time()

l=[1,0]*500000
l[1],l[2]=1,0
v=3
while v<1000000:
    if not l[v]:
        i=v*3
        while i<1000000:
            l[i]=1
            i+=2*v
    v+=2

S=0
b=0
for x in range(2,500000):
    if not l[x]:
        S+=x
    if S>1000000:
        b=x
        break

for x in range(b,1,-1):
    if not l[x]:
        S-=x
    if S%2==0:
        if not l[S-5]:
            S-=5
            break
        elif not l[S-17]:
            S-=17
            break
    else:
        if not l[S]:
            break
        elif not l[S-2]:
            S-=2
            break
        elif not l[S-10]:
            S-=10
            break
        elif not l[S-28]:
            S-=28
            break

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
