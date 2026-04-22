# Problem 21
import math

def divisors_sum(n):
    if n==1: return 0
    total=1
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            if i * i == n:
                total += i
            else:
                total += i + n // i
    return total

#n=220
#print(divisors_sum(n))

def amicable_numbers(dictionary,N):
    for n in range(1,N+1):
        if n not in dictionary:
            if divisors_sum(divisors_sum(n)) == n and divisors_sum(n) != n:
                dictionary[n]=True
                if divisors_sum(n) < N: dictionary[divisors_sum(n)]=True
            else: 
                dictionary[n]=False
    return

dictionary={}
N=10000
amicable_numbers(dictionary,N)
total=sum(k for k, is_true in dictionary.items() if is_true)
print(f"the sum is {total}")
