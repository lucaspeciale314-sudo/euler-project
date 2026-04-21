# Problem 20
# defined the factorial, getting rid of the extra zeroes
def zeroless_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
        if i%5 == 0: fact //= 10
        if i%25 == 0: fact //= 10
    return fact

N=zeroless_factorial(100)
digits=[int(k) for k in str(N)]
digits_sum=0
for d in digits: digits_sum += d
print(f"{digits_sum}")
