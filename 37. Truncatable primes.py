import time

start=time.time()

marked =[1,0]*5000000
marked[1]=1
marked[2]=0
num=3
S=0-3-5-7
t=0
while t<14 and num<10000000:
    if not marked[num]:
        sn=str(num)
        l=len(sn)
        rst=True
        if sn[0] in ("2","3","5","7") and sn[l-1] in ("3","7"):
            for x in range(1,l):
                if marked[int(sn[x:])]:
                    rst=False
                    break
                if marked[int(sn[:l-x])]:
                    rst=False
                    break
            if rst==True:
                S+=num
                t+=1
                print(num,t)
        i=num*2
        while i<10000000:
            marked[i] = 1
            i+=num
    num+=2

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
