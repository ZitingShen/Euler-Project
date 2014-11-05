import time

start=time.time()

v={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def royalflush(p):
    if [p[0][0],p[1][0],p[2][0],p[3][0],p[4][0]]==['A','J','K','Q','T'] and p[0][1]==p[1][1]==p[2][1]==p[3][1]==p[4][1]:
        return 1
    else:
        return 0
def straightflush(p):
    l=[v[p[0][0]],v[p[1][0]],v[p[2][0]],v[p[3][0]],v[p[4][0]]]
    if sorted(l) in [2,3,4,5,6,7,8,9,10,11,12,13,14] and p[0][1]==p[1][1]==p[2][1]==p[3][1]==p[4][1]:
        return max(l)
    else:
        return 0
def fourofakind(p):
    if p[0][0]==p[1][0]==p[2][0]==p[3][0] or p[1][0]==p[2][0]==p[3][0]==p[4][0]:
        return v[p[1][0]]
    else:
        return 0
def fullhouse(p):
    if (p[0][0]==p[1][0]==p[2][0] and p[3][0]==p[4][0]) or (p[2][0]==p[3][0]==p[4][0] and p[0][0]==p[1][0]):
        return v[p[2][0]]
    else:
        return 0
def flush(p):
    if  p[0][1]==p[1][1]==p[2][1]==p[3][1]==p[4][1]:
        return v[p[4][0]]
    else:
        return 0
def straight(p):
    l=[v[p[0][0]],v[p[1][0]],v[p[2][0]],v[p[3][0]],v[p[4][0]]]
    if sorted(l) in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
        return max(l)
    else:
        return 0
def threeofakind(p):
    if p[0][0]==p[1][0]==p[2][0] or p[1][0]==p[2][0]==p[3][0] or p[2][0]==p[3][0]==p[4][0]:
        return v[p[2][0]]
    else:
        return 0
    if (ps[0][0]==ps[1][0] and ps[2][0]==ps[3][0]) or (ps[1][0]==ps[2][0] and ps[3][0]==ps[4][0]) or (ps[0][0]==ps[1][0] and ps[3][0]==ps[4][0]):
        i+=1
    if ps[0][0]==ps[1][0] or ps[1][0]==ps[2][0] or ps[2][0]=ps[3][0] or ps[3][0]==ps[4][0]:
        i+=1
    
        
S=0
with open("C:/Users/lenovo/Desktop/poker.txt","r") as textfile:
    for line in textfile:
        line=line.rstrip('\n').split()
        p1=sorted(line[:5])
        p2=sorted(line[5:])
        if royalflush(p1)>royalflush(p2):
            S+=1
        elif straightflush(p1)>straightflush(p2):
            S+=1
        elif fourofakind(p1)>fourofakind(p2):
            S+=1
        elif fullhouse(p1)>fullhouse(p2):
            S+=1
        elif flush(p1)>flush(p2):
            S+=1
        elif straight(p1)>straight(p2):
            S+=1

elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
