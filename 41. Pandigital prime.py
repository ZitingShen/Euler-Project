import time

start=time.time()

d=False
i=7654321
while d==False:
    string="".join(sorted(str(i)))
    if "1" in string and string in "1234567":
        l=0
        for x in range(2,int(i**0.5)+1):
            if i%x==0:
                l=1
                break
        if not l:    
            S=i
            d=True
    i-=2

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
