def divisor(n):
    a=0
    nroot=int(n**0.5)
    for p in range(1,nroot):
        if n%p==0:
            a+=2
    if i**0.5==nroot:
        a+=1
    return a

i=3
k=False
while k==False:
    a=0
    if i%2!=0:
        if divisor(i)*divisor((i+1)/2)>500:
            k=True
        else:
            i+=1
    else:
        if divisor(i/2)*divisor(i+1)>500:
            k=True
        else:
            i+=1
print(sum(range(1,i+1)))
