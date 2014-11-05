import time

start=time.time()

marked = [1,0]*500000
marked[1]=1
marked[2]=0
value=3
while value<1000000:
    if not marked[value]:
        i=value*2
        while i < 1000000:
            marked[i]=1
            i+=value
    value+=2


for p in range(1000000):
    if not marked[p]:
        sp=str(p)
        for x in range(1,len(sp)):
            if marked[int(sp[x:]+sp[:x])]:
                marked[p]=1
                break

S=1000000-sum(marked)

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
