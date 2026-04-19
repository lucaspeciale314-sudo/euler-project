#Problem 12: Triangular numbers factors
import math

def eratosthenes_sieve(bound):
    if bound < 2:
        return []
      
    is_prime = [True] * (bound + 1)
    is_prime[0] = False
    is_prime[1] = False
  
    for p in range(2, math.isqrt(bound) + 1):
        if is_prime[p]:
            for multiple in range(p * p, bound + 1, p):
                is_prime[multiple] = False
              
    primes = []
  
    for n in range(2, bound + 1):
        if is_prime[n]:
            primes.append(n)

    return primes


def dividing_primes(N):
    """
    Return the prime factors of N, with repetition.
    """

    # Base case:
    # if N is less than 2, there is nothing left to factor.
    if N < 2:
        return []
    # There is going to be a prime factor less or equal to the square root unless N is prime  
    primes = eratosthenes_sieve(math.isqrt(N))

    for p in primes:
        if N % p == 0:
            return [p] + dividing_primes(N // p)

    return [N]

def counting_divisors(increasing_prime_factorization)
