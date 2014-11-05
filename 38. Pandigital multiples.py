import time

start=time.time()

S=918273645
for x in range(9182,9877):
    if "".join(sorted(str(x)+str(2*x)))=="123456789":
        S=int(str(x)+str(2*x))

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
