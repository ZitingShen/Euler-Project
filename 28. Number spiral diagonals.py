import time

start=time.time()

S=1
for x in range(1,501):
    S+=16*x**2+4*x+4
           
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
