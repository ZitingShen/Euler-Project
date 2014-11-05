import time

start=time.time()

def factors(x):
    for y in range(x//2,1,-1):
        if x%y==0:
            if y%(x//y)==0:
                return [l[y]]
            else:
                return [l[y]+1]
    return [1]

num=4
l=[0]*2+[1]*2
stop=False
while not stop:
    l+=factors(num)
    if l[num]==4:
        if l[num-1]==4:
            if l[num-2]==4:
                if l[num-3]==4:
                    S=num-3
                    stop=True
    num+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))#2029 seconds
