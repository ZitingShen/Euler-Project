import time

start=time.time()

stop=False
i=1
while not stop:
    l=sorted(str(i))
    if sorted(str(2*i))==l:
        if sorted(str(3*i))==l:
            if sorted(str(4*i))==l:
                if sorted(str(5*i))==l:
                    if sorted(str(6*i))==l:
                        S=i
                        stop=True
    i+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
