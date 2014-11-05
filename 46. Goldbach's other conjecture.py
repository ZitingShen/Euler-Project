import time

start=time.time()

def isconjecture(x):
    if (x/2)**0.5%1==0:
        return True
    else:
        return False

def isprime(x):
    for y in range(3,int(x**0.5)+1):
        if x%y==0:
            return False
    return True

S=1
ps=[]
stop=False
while not stop:
    S+=2
    if isprime(S):
        ps.append(S)
    else:
        stop=True
        for p in ps:
            if isconjecture(S-p):
                stop=False
                break

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
