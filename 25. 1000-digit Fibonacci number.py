import time

start=time.time()

num1=1
num2=1
S=2
while len(str(num2))<1000:
    num3=num1+num2
    num1=num2
    num2=num3
    S+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
