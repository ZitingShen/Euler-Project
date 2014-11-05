import time
 
start = time.time()

with open("C:/Users/lenovo/Desktop/names.txt","r") as textfile:
    names=textfile.read().split(',')

names.sort()
alpha={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,
       'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
       'V':22,'W':23,'X':24,'Y':25,'Z':26}

S=0
for x in range(len(names)):
    summ=0
    for y in range(1,len(names[x])-1):
        summ+=alpha[names[x][y]]
    S+=(x+1)*summ


elapsed = (time.time() - start)
print("found %s in %s seconds" % (S,elapsed))
