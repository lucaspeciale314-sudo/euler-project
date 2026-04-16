# This script is incredibly slow
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
        
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

def main():
    # Keep running until it's done without errors as requested
    while True:
        try:
            n_str = input("Please enter a positive number n: ")
            n = int(n_str)
            if n < 1:
                print("n must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    primes = sieve_of_eratosthenes(n)
    
    count = 0
    for x in range(1, n + 1):
        val = x * x + 1
        # Check if divisible by p^2 for any prime p <= n
        for p in primes:
            if val % (p * p) == 0:
                count += 1
                break # We just count how many x's satisfy the condition
                
    result = n - count
    print(f"Result: there are {result} values of x^2 + 1 (for x between 1 and {n}) that are NOT divisible by p^2 for any prime p <= {n}.")

if __name__ == "__main__":
    main()
