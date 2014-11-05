import time
 
start = time.time()


k=(366+365*3)*25+365
days=[0]*k

i=0
while 7*i+6<k:
    days[7*i+6]=1
    i+=1

times=0
date=365
for m in range(1,1200):
    if days[date]==1:
        times+=1
    if m%12 in [0,1,3,5,7,8,10]:
        date+=31
    elif m%12 in [4,6,9,11]:
        date+=30
    elif m%48 in [2,14,26]:
        date+=28
    elif m%48==38:
        date+=29
    

S=times

elapsed = (time.time() - start)
print("found %s in %s seconds" % (S,elapsed))
