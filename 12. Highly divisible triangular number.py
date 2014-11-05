i=1
k=False
while k==False:
    num=sum(range(1,i+1))
    numroot=int(num**0.5)
    divisor=0
    for p in range(1,numroot):
        if num%p==0:
            divisor+=2
    if num%numroot==0:
        divisor+=1
    if divisor>=500:
        k=True
    else:
        i=i+1
print(num)
