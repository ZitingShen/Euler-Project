import time

start=time.time()

def palindrome(x):
    l=len(x)
    if l%2==0:
        for y in range(l//2):
            if x[y]!=x[l-y-1]:
                return False
        return True
    else:
        for y in range((l-1)//2):
            if x[y]!=x[l-y-1]:
                return False
        return True

S=0
for x in range(1000000):
    sx=str(x)
    if palindrome(sx):
        sx2=bin(x)[2:]
        if palindrome(sx2):
            S+=x

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
