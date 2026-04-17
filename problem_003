# We import the module "math" because it contains mathematical functions.
# In particular, we use:
# - math.sqrt(x)   to compute the square root of x
# - math.ceil(x)   to round a real number upward to the nearest integer
import math


def sieve_of_eratosthenes(limit):
    """
    Return the list of all prime numbers <= limit
    using the Sieve of Eratosthenes.

    The idea is the classical one:
    - start by assuming every integer from 2 to 'limit' is prime;
    - then cross out multiples of 2;
    - then multiples of 3;
    - and so on.
    What remains uncrossed are exactly the prime numbers.
    """

    # If limit < 2, there are no primes at all.
    if limit < 2:
        return []

    # This list contains True/False values.
    # Position i corresponds to the integer i.
    # At the beginning we assume every number is prime.
    is_prime = [True] * (limit + 1)

    # But 0 and 1 are not prime by definition.
    is_prime[0] = False
    is_prime[1] = False

    # To run the sieve, it is enough to check divisors only up to sqrt(limit).
    max_check = int(math.sqrt(limit))

    # Loop through possible prime bases p = 2, 3, 4, ..., floor(sqrt(limit))
    for p in range(2, max_check + 1):

        # If p is still marked as prime, cross out its multiples.
        if is_prime[p]:

            # Start from p*p.
            # Smaller multiples of p have already been handled before.
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    # Collect all numbers that remained marked as prime.
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


def largest_prime_factor_by_requested_method(n):
    """
    Compute the largest prime divisor of n using exactly the method requested.

    The algorithm works as follows:

    1. Start from the original number n.
    2. Compute ceil(sqrt(current number)).
    3. Build all primes up to that bound with the sieve.
    4. Test divisibility starting from the largest such prime and going downward.
    5. As soon as one divisor is found, divide by it and continue.
    6. Keep in memory ONLY the first prime divisor ever found.
    7. Stop when:
       - no divisor is found (then the current number is prime), or
       - the quotient becomes smaller than sqrt(original n).
    """

    # We keep the original number because your stopping condition
    # compares the later quotients with sqrt(original n).
    original_n = n

    # This is ceil(sqrt(n)) for the original input n.
    original_bound = math.ceil(math.sqrt(original_n))

    # This variable will be updated step by step:
    # n, then n_1 = n/p, then n_2 = n_1/q, etc.
    current_n = n

    # This will store the FIRST prime divisor found.
    # It is set only once and then never overwritten.
    first_found_prime = None

    while True:
        # Compute ceil(sqrt(current_n)).
        current_bound = math.ceil(math.sqrt(current_n))

        # Generate all primes up to this bound.
        primes = sieve_of_eratosthenes(current_bound)

        # This remembers whether a divisor was found in this round.
        found_divisor = False

        # We inspect primes from largest to smallest, exactly as requested.
        for p in reversed(primes):

            # The symbol % is the "remainder" operator.
            # current_n % p == 0 means that p divides current_n exactly.
            if current_n % p == 0:
                found_divisor = True

                # Store the first found prime divisor only once.
                if first_found_prime is None:
                    first_found_prime = p

                # Replace current_n by current_n / p.
                # The operator // is integer division:
                # for example, 84 // 7 = 12.
                current_n = current_n // p

                # We stop immediately after the first divisor found in this round.
                break

        # If no divisor was found, then current_n is prime.
        if not found_divisor:
            return current_n

        # If current_n has now become smaller than sqrt(original n),
        # then by your rule the answer is the FIRST prime divisor found.
        if current_n < original_bound:
            return first_found_prime


def main():
    """
    Ask the user for an integer > 1,
    apply the algorithm,
    and print the result.
    """

    # input(...) always returns text, called a "string" in programming.
    user_input = input("Insert an integer greater than 1: ")

    # Try to convert the text into an integer.
    try:
        n = int(user_input)
    except ValueError:
        print("Error: you must insert an integer.")
        return

    # We only allow integers greater than 1.
    if n <= 1:
        print("Error: the number must be greater than 1.")
        return

    answer = largest_prime_factor_by_requested_method(n)

    # If the answer is n itself, then n is prime.
    if answer == n:
        print(f"{n} is prime.")
        print(f"The biggest prime dividing {n} is {answer}.")
        print(f"Factorization in the requested form: {n} = {answer} * 1")
    else:
        # The "remaining cofactor" is whatever remains when dividing n by answer.
        # We do not factor it further here; we just display it.
        cofactor = n // answer

        print(f"The biggest prime dividing {n} is {answer}.")
        print(f"Factorization: {n} = {answer} * {cofactor}")


# This means:
# run main() only if this file is executed directly,
# not if it is imported from another Python file.
if __name__ == "__main__":
    main()
