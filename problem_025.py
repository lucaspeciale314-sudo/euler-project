import math
LIMIT=1000
def Fib(m):
    Phi=(1+math.sqrt(5))/2
    # We use an approximation as computing Phi^m would become too heavy
    d_m = math.log10((Phi)) * m - math.log10(math.sqrt(5))
    return int(d_m)+1
n=2
fibonacci_dig=1
while fibonacci_dig < LIMIT: 
    n += 1
    fibonacci_dig = Fib(n)

print(n)
