product=2**1000
string=str(product)
print(sum(int(string[x]) for x in range(0,len(string))))
