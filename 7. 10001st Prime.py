i=2
num=3
primes=[3]
while i<10001:
    num+=2
    rst=True
    for p in primes:
        if num%p==0:
            rst=False
            break
    if rst==True:
        i+=1
        primes.append(num)
        print(num)
