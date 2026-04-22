# Problem 21
import math

def divisors_sum(n):
    sum=1
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: 
            sum += i+n//i 
            #print(i)
    return sum

#n=220
#print(divisors_sum(n))

def amicable_numbers(dictionary,N):
    for n in range(1,N+1):
        if n not in dictionary:
            if divisors_sum(divisors_sum(n)) == n and divisors_sum(n) != n:
                dictionary[n]=True
                dictionary[divisors_sum(n)]=True
            else: dictionary[n]=False
    return

dictionary={}
N=10000
amicable_numbers(dictionary,N)
sum_=sum(k for k, is_true in dictionary.items() if is_true)
print(f"the sum is {sum_}")
