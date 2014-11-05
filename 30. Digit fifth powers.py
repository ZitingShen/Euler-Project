import time

start=time.time()

S=0
for x in range(10,1000000):
    s=str(x)
    p=0
    for y in range(len(s)):
        p+=int(s[y])**5
    if x==p:
        S+=x
           
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
