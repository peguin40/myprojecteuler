# find first triangle number with over 500 divisors
j=0
num=0
divisor_count=1
while divisor_count<500:
    j+=1
    num+=j
    divisor_count=0
    for i in range(1,int(num**(1/2))+1):
        if num%i==0:
            divisor_count+=2

print(num)
