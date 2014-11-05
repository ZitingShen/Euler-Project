import time

start=time.time()

a=1
b=1
for x in range(11,100):
    for y in range(10,x):
        sx=str(x)
        sy=str(y)
        if sx[0]==sy[0] and sx[1]!="0":
            if y/x==int(sy[1])/int(sx[1]):
                a*=x
                b*=y
        if sx[0]==sy[1] and sx[1]!="0":
            if y/x==int(sy[0])/int(sx[1]):
                a*=x
                b*=y
        if sx[1]==sy[0]:
            if y/x==int(sy[1])/int(sx[0]):
                a*=x
                b*=y
        if sx[1]==sy[1] and sx[1]!="0":
            if y/x==int(sy[0])/int(sx[0]):
                a*=x
                b*=y

S=b/a
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
