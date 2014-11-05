import time

start=time.time()

rst=[0]*10000
for x in range(12345,98766):
    s=str(x)
    p1=int(s[0]+s[1])*int(s[2]+s[3]+s[4])
    p2=int(s[0])*int(s[1]+s[2]+s[3]+s[4])
    sp1=str(p1)
    sp2=str(p2)
    if "".join(sorted(s+sp1))=="123456789":
        rst[p1]=1
    if "".join(sorted(s+sp2))=="123456789":
        rst[p2]=1

S=0
for x in range(10000):
    if rst[x]==1:
        S+=x
           
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
