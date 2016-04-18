smallest_multiple=2520
for i in range(1,21):
    factors=[]
    current=i
    j=2
    while current!=1:
        if current%j==0 and j!=i:
            factors.append(j)
            current=current//j
            j=2
        elif j==i and factors==[]:
            factors.append(j)
            break
        else:
            j+=1
    temp=smallest_multiple
    for k in factors:
        if temp%k!=0:
            smallest_multiple*=k
        else:
            temp=temp/k
print(smallest_multiple)
