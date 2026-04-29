import math
LIMIT=1000
Phi = (1+math.sqrt(5))/2
LOG_SQRT5 = math.log10(math.sqrt(5))
def fibonacci_digits(m):
    # We use log10(F_m) ~ m log10(phi) - log10(sqrt(5)),
    # since computing phi**m would become too large.
    d_m = math.log10((Phi)) * m - LOG_SQRT5 
    return int(d_m)+1
n=2
fibonacci_dig=1
while fibonacci_dig < LIMIT: 
    n += 1
    fibonacci_dig = fibonacci_digits(n)

print(n)
