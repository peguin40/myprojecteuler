a=2
first=1
second=2
exceed=True

while exceed:
    first=first+second
    if first<4000000:
        if first%2==0:
            a+=first
    else:
        exceed=False
    second=second+first
    if second<4000000:
        if second%2==0:
            a+=second
    else:
        exceed=False
        
print(a)
