import time

start=time.time()

def ispentagon(x):
    if ((24*x+1)**0.5+1)%6==0:
        return True
    else:
        return False
        

l=[1]
i=2
d=0
k=True
while k:
    l.append((3*i**2-i)//2)
    for x in range(i-2,-1,-1):
        if ispentagon(l[i-1]-l[x]) and ispentagon(l[i-1]+l[x]):
            d=l[i-1]-l[x]
            break
    if d:
        if l[i-1]-l[i-2]>d:
            k=False
    i+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (d,elapsed))
