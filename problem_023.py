# Problem 23: Sum of non-abundant numbers 
# We also print the complete list at the end
import math
def divisors_sum(n):
    if n==1: return 0
    total=1
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            if i * i == n:
                total += i
            else:
                total += i + n // i
    return total
LIMIT = 28123
abundant_numbers=[]

for k in range(1,LIMIT + 1):
    if divisors_sum(k) > k: abundant_numbers.append(k)

#print(abundant_numbers)

sum_of_two_abundant_numbers=set()

for i, a in enumerate(abundant_numbers):
    for b in abundant_numbers[i:]:
        s=a+b
        if a+b > 28123: break 
        sum_of_two_abundant_numbers.add(s)
        
sum_nonabundant_numbers = sum(
    n for n in range(1, LIMIT + 1)
    if n not in sum_of_two_abundant_numbers
)

print(sum_nonabundant_numbers)

list_nonabundant_numbers=[n for n in range(1,LIMIT + 1) if n not in sum_of_two_abundant_numbers ]
print(f" Here is the list of all non-abundant numbers: {list_nonabundant_numbers}")
