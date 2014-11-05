import time

start=time.time()

Biggest=0
for a in range(-999,1000,2):
    for b in range(3,1000,2):
        n=0
        rst=True
        num=0
        while rst==True:
            t=n**2+a*n+b
            if t<3:
                break
            else:
                num+=1
                for x in range(3,int(t**0.5)+1,2):
                    if t%x==0:
                        rst=False
                        num-=1
                        break
                n+=1
        if num>Biggest:
            Biggest=num
            S=a*b
           
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
