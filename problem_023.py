import math
def divisors_sum(n):
    if n==1: return 0
    total=1
    for i in range(2,int(math.isqrt(n))+1):
        if n % i == 0:
            if i * i == n:
                total += i
            else:
                total += i + n // i
    return total
    
abundant_numbers=[]

for k in range(1,28124):
    if divisors_sum(k) > k: abundant_numbers.append(k)

#print(abundant_numbers)

sum_of_two_abundant_numbers=set()

for i, a in enumerate(abundant_numbers):
    for b in abundant_numbers[i:]:
        s=a+b
        if a+b <= 28123: break 
        sum_of_two_abundant_numbers.add(s)
        
numbers={}
sum_nonabundant_numbers=0
for k in sum_of_two_abundant_numbers:
    numbers[k]= False
for i in range(1,28124):
    if i not in numbers: numbers[i]=True

for l in numbers:
    if numbers[l] == True: sum_nonabundant_numbers += l

print(sum_nonabundant_numbers)
