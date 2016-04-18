largest_factor=0
for i in range(1,int(600851475143**(1/2))):
    if 600851475143%i==0 and i>largest_factor:
        k=600851475143/i
        for j in range(2,int(i**(1/2))):
            if i%j==0:
                break
            elif j==int(i**(1/2))-1:
                largest_factor=i
        if k >largest_factor:
            for j in range(2,int(k**(1/2))):
                if k%j==0:
                    break
                elif j==int(k**(1/2))-1:
                    largest_factor=k
print(largest_factor)
