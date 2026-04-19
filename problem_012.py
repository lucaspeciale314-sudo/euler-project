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
    # There is going to be a prime factor less or equal to the square root unless N is prime (we could probably optimize more since N is triangular 2N=n(n+1), but we should avoid recursion )
    primes = eratosthenes_sieve(math.isqrt(N))

    for p in primes:
        if N % p == 0:
            return [p] + dividing_primes(N // p)

    return [N]

def counting_divisors(grouped_prime_factors):
    """
    Input:
        a sorted list of prime factors with repetition
        e.g. [2, 2, 2, 3, 3, 5]

    Output:
        the number of positive divisors of the original number
    """

    # Special case: N = 1
    if grouped_prime_factors == []:
        return 1

    number_of_divisors = 1
    current_power = 1

    # We start from index 1 because we compare each entry
    # with the previous one.
    for i in range(1, len(grouped_prime_factors)):
        if grouped_prime_factors[i] == grouped_prime_factors[i - 1]:
            current_power += 1
        else:
            number_of_divisors *= (current_power + 1)
            current_power = 1

    # Account for the last prime block
    number_of_divisors *= (current_power + 1)

    return number_of_divisors
lot_divisors=1
for i in range(4, 15000):
    T=i*(i+1)//2
    if i%2==0:
        new_count=counting_divisors(dividing_primes(i//2)+dividing_primes(i+1))
    else:    
        new_count=counting_divisors(dividing_primes((i+1)//2)+dividing_primes(i))
    if new_count > lot_divisors:
        lot_divisors=new_count
    if lot_divisors>500:
        print(f"The number of divisors exceeds 500 for T_n, with n={i}, and T_n={T}")
        break
print(f"The maximum number of divisors achieve in this range is {lot_divisors}")
"""
This is (quite) a bit slower
for i in range(4, 1000)
    T=i*(i+1)//2
    new_count=counting_divisors(dividing_primes(T))
    if new_count > lot_divisors
        lot_divisors=new_count
    if lot_divisors>500
        print(f"The number of divisors exceeds 500 for T_n, with n={i}, and T_n={T}")
        break
print(f"The maximum number of divisors achieve in this range is {lot_divisors}")
"""

    
