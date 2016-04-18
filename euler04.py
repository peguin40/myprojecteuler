largest_palindrome=0
for i in range(100,1000):
    for j in range(100,1000):
        product=str(i*j)
        if product==product[::-1] and int(product)>largest_palindrome:
            largest_palindrome=int(product)

print(largest_palindrome)
