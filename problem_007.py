#Problem 7: Let's implement a sieve using the known "density of primes" N/log(N) to get a 'minimal' upper bound.
import math
def sieve_bound():
    for i in range(100010,1000000,10):
        if i/math.log(i)>10010:
            print(i)
            return i
            
#N=sieve_bound()
def sieve(N):
    # We create a list of truth values.
    # At the beginning, we assume every number is prime.
    is_prime = [True] * (N + 1)

    # 0 and 1 are not prime by definition.
    if N >= 0:
        is_prime[0] = False
    if N >= 1:
        is_prime[1] = False

    # We only need to test divisors up to sqrt(N),
    # i.e. while p*p <= N.
    p = 2
    while p * p <= N:
        if is_prime[p]:
            # If p is prime, then all multiples of p
            # starting from p*p are not prime.
            for multiple in range(p * p, N + 1, p):
                is_prime[multiple] = False
        p += 1

    # Build the list of actual prime numbers.
    primes = []
    for k in range(2, N + 1):
        if is_prime[k]:
            primes.append(k)

    return primes

def main():  
    N=sieve_bound()
    P=sieve(N)
    print("Number of primes found:", len(P))
    print("The 10001st prime is:", P[10000])
    
if __name__ == "__main__":
    main()
