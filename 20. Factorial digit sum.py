import time
 
start = time.time()

product=1
for x in range(1,101):
    product*=x
string=str(product)
l=len(string)
S=0
for x in range(0,l):
    S+=int(string[x])

elapsed = (time.time() - start)
print("found %s in %s seconds" % (S,elapsed))
