for a in range(1,500):
    bmin=501-a
    for b in range(bmin,500):
        if a**2+b**2==(1000-a-b)**2:
            print(a*b*(1000-a-b))
            break
