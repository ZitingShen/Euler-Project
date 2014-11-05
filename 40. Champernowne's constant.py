import time

start=time.time()

l="0"
for x in range(1,1000000):
    l+=str(x)

S=int(l[1])*int(l[10])*int(l[100])*int(l[1000])*int(l[10000])*int(l[100000])*int(l[1000000])


elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
