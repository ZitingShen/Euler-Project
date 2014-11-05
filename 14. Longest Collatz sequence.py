import time
 
start = time.time()

l=[0]*999999
chain=0
S=0
for i in range(999999,333333,-1):
    if not l[i-1]:
        num=0
        a=i
        while a!=1:
            if a%2==0:
                a=a/2
            else:
                a=3*a+1
            if a<100000:
                l[int(a)-1]=1
            num+=1
        if num>chain:
            chain=num
            print(i)
            S=i
    

elapsed = (time.time() - start)
print("found %s in %s seconds" % (S,elapsed))
