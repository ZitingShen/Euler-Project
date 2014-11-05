import time

start=time.time()

S=99*81
for x in [2,3,5,6,7,10]:
    l=[0]*600
    for y in range(1,7):
        if x**y<101:
            for z in range(2,101):
                l[y*z-1]=1
    S+=sum(l)       
           
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
