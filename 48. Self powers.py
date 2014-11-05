import time

start=time.time()

rst=0
for x in range(1,1001):
    rst+=x**x

S=str(rst)[-10:]

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
