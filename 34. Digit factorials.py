import time

start=time.time()

S=0
l=[1,1,2,6,24,120,720,5040,40320,362880]
for x in range(10,2540161):
    sx=str(x)
    p=0
    for y in sx:
        p+=l[int(y)]
    if p==x:
        S+=x

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
