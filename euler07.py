num_prime=0
current=2
current_prime=2
def is_prime(n):
    for i in range(2,int(n**(1/2))):
        if n%i==0:
            return False
        elif i==int(n**(1/2)):
            return True
    return True
        
while num_prime<10001:
    if current**(1/2)<2:
        num_prime+=1
        current_prime=current
        current+=1
    elif current**(1/2)==int(current**(1/2)):
        current+=1
    else:
        if is_prime(current):
            num_prime+=1
            current_prime=current
            current+=1
        else:
            current+=1
print(current_prime)
