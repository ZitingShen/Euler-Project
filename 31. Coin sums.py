import time

start=time.time()

S=0
for a in range(2):
    if 200*a==200:
        S+=1
    else:
        for b in range(3):
            if 200*a+100*b==200:
               S+=1
            elif 200*a+100*b>200:
                break
            else:
                for c in range(5):
                    if 200*a+100*b+50*c==200:
                        S+=1
                    elif 200*a+100*b+50*c>200:
                        break
                    else:
                        for d in range(11):
                            if 200*a+100*b+50*c+20*d==200:
                                S+=1
                            elif 200*a+100*b+50*c+20*d>200:
                                break
                            else:
                                for e in range(21):
                                    if 200*a+100*b+50*c+20*d+10*e==200:
                                        S+=1
                                    elif 200*a+100*b+50*c+20*d+10*e>200:
                                        break
                                    else:
                                        for f in range(41):
                                            if 200*a+100*b+50*c+20*d+10*e+5*f==200:
                                                S+=1
                                            elif 200*a+100*b+50*c+20*d+10*e+5*f>200:
                                                break
                                            else:
                                                for g in range(101):
                                                    if 200*a+100*b+50*c+20*d+10*e+5*f+2*g<201:
                                                        S+=1
                                                    else:
                                                        break
           
elapsed=(time.time()-start)
print ("found %s in %s seconds" % (S,elapsed))
