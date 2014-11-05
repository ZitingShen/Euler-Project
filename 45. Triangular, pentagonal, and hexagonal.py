import time

start=time.time()

def ispentagonal(x):
    if ((24*x+1)**0.5+1)%6==0:
        return True
    else:
        return False

def istriangle(x):
    if ((8*x+1)**0.5-1)%2==0:
        return True
    else:
        return False

i=143
stop=False
while not stop:
    i+=1
    S=i*(2*i-1)
    if ispentagonal(S):
        if istriangle(S):
            stop=True        

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
