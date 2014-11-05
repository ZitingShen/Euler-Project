import time

start=time.time()

def new(string,denominator):
    l=[]
    for x in range(10):
        if str(x) not in string:
            if (100*x+int(string[0:2]))%denominator==0:
                l.append(str(x)+string)
    return l


nums1=[]
nums2=[]
for x in range(100,1000):
    if x%17==0:
        l=str(x)
        if l[0]!=l[1] and l[1]!=l[2] and l[2]!=l[0]:
            nums1+=new(l,13)

for num1 in nums1:
    nums2+=new(num1,11)

nums1=[]
for num2 in nums2:
    nums1+=new(num2,7)

nums2=[]
for num1 in nums1:
    nums2+=new(num1,5)

nums1=[]
for num2 in nums2:
    nums1+=new(num2,3)

nums2=[]
for num1 in nums1:
    nums2+=new(num1,2)

nums1=[]
for num2 in nums2:
    nums1+=new(num2,1)

S=0
for num1 in nums1:
    if num1[0]!=0:
        S+=int(num1)         

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
