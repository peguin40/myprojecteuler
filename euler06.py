sum_indiv_sqr=0
sum_all=0
for i in range(1,101):
    sum_all+=i
    sum_indiv_sqr+=i**2
sum_all_sqr=sum_all**2

print(sum_all_sqr-sum_indiv_sqr)
