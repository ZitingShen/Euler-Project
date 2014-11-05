l=[1,0]*500000
l[1],l[2]=1,0
v=3
while v<1000000:
    if not l[v]:
        i=v*3
        while i<1000000:
            l[i]=1
            i+=2*v
    v+=2

for x in range(10000,1000000):
    s=str(x)
    if sorted(s)[:3]==['1','1','1'] and x%10 in [1,3,7,9]:
        for a in range(len(s)-3):
            if s[a]=='1':
                for b in range(a+1,len(s)-2):
                    if s[b]=='1':
                        for c in range(b+1,len(s)-1):
                            if s[c]=='1':
                                ll=[]
                                for y in range(10):
                                    if y:
                                        if not l[int(s[:a]+str(y)+s[a+1:b]+str(y)+s[b+1:c]+str(y)+s[c+1:])]:
                                            ll+=[int(s[:a]+str(y)+s[a+1:b]+str(y)+s[b+1:c]+str(y)+s[c+1:])]
                                    else:
                                        if len(str(int(s[:a]+'0'+s[a+1:b]+'0'+s[b+1:c]+'0'+s[c+1:])))==len(s):
                                            if not l[int(s[:a]+'0'+s[a+1:b]+'0'+s[b+1:c]+'0'+s[c+1:])]:
                                                ll=[int(s[:a]+'0'+s[a+1:b]+'0'+s[b+1:c]+'0'+s[c+1:])]
                                if len(ll)>7:
                                    print(ll)
