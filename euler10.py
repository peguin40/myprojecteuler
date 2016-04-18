current=3
sum_primes=2
def is_prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n%i==0:
            return False
    return True
while current<2000000:
    if is_prime(current)==True:
        sum_primes+=current
    current+=2
print(sum_primes)
