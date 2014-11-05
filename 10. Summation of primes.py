numbers=[i*2+1 for i in range(1,1000000)]
i=0
m=3
root=int(2000000**0.5)
half=1000000-1
while m<=root:
        if numbers[i]:
            j=int((m*m-3)/2)
            numbers[j]=0
            while j<half:
                numbers[j]=0
                j+=m
        i=i+1
        m=2*i+3
print(sum(numbers)+2)
