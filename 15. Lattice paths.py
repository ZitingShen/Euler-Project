def product(m,n):
    result=1
    for i in range(m,n+1):
        result*=i
    return result

print(product(21,40)/product(1,20))
