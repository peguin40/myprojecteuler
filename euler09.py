for m in range(1,334):
    for n in range(m+1,334):
        a=n**2-m**2
        b=2*n*m
        c=n**2+m**2
        if a+b+c==1000:
            print(a*b*c)
