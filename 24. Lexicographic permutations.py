import time

start=time.time()

p=9*8*7*6*5*4*3*2
rest=1000000
nums=[0]*10
num=[]
for x in range(1,11):
    if rest%p!=0:
        t=0
        i=-1
        while t<=int(rest/p):
            i+=1
            if not nums[i]:
                t+=1
        num.append(i)
        nums[num[x-1]]=1
        print(nums)
        rest-=p*(int(rest/p))
        if x!=10:
            p=p//(10-x)
        print(rest,p)
    else:
        t=0
        i=-1
        while t<rest/p:
            i+=1
            if not nums[i]:
                t+=1
        num.append(i)
        print("do the rest yourself! Just put the large numbers before small ones!")
        break

S=''
for x in range(len(num)):
    S+=str(num[x])

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
