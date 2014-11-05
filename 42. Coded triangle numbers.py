import time

start=time.time()

with open("C:/Users/lenovo/Desktop/words.txt","r") as textfile:
    words=textfile.read().split(",")

alpha={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,
       'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
       'V':22,'W':23,'X':24,'Y':25,'Z':26,'"':0}

n=1
triangles=[]
while n*(n+1)/2<=1300:
    triangles.append(n*(n+1)//2)
    n+=1

S=0
for word in words:
    rst=0
    for letter in word:
        rst+=alpha[letter]
    if rst in triangles:
        S+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
