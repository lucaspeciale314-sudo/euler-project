def sieve_of_eratosthenes(limit):
    """
    This function implements the Sieve of Eratosthenes.
    It takes an integer 'limit' (our upper bound n) and returns a list of all 
    prime numbers less than or equal to 'limit'. 
    """
    
    # In Python, we can create a list (similar to an ordered set or array).
    # Here, we create a list of boolean (True/False) truth values.
    # '[True] * (limit + 1)' creates a list of 'limit + 1' elements, all set to True.
    # We use 'limit + 1' because Python uses 0-based indexing (counting starts at 0). 
    # This aligns the index of the list perfectly with the number we are evaluating. 
    # (e.g., is_prime[2] will tell us if the number '2' is prime).
    is_prime = [True] * (limit + 1)
    
    # 0 and 1 are defined mathematically as not prime, so we explicitly set them to False.
    # We access and change specific elements in the list using bracket notation.
    is_prime[0] = False
    is_prime[1] = False
    
    # We only need to test numbers up to the square root of our limit.
    # In Python, 'limit**0.5' is the mathematical equivalent of raising to the 1/2 power (√limit).
    # 'int()' takes the integer part (floor) of the resulting value, since array indices must be whole numbers.
    # The 'range(start, target)' function generates a sequence of integers from 
    # 'start' up to, but strictly LESS THAN, 'target'. Since we want to include the integer 
    # part of the square root, we add 1.
    bound = int(limit**0.5) + 1
    
    # This is a 'for loop'. It iterates through each integer 'p' in our generated range.
    # Think of it as the mathematical formulation: "∀ p ∈ {2, 3, ..., bound-1}"
    for p in range(2, bound):
        # 'if' is a conditional statement. It executes the block below it if the statement is True.
        # If is_prime[p] is True, then p hasn't been crossed out, meaning it is a prime number.
        if is_prime[p]:
            
            # If p is prime, we must cross out all of its multiples.
            # We can start crossing out multiples from p^2, since any smaller multiple of p 
            # (like p * q, where q < p) would have already been crossed out when we evaluated q.
            # 'range(p*p, limit + 1, p)' generates integers starting at p^2, 
            # going up to 'limit' (limit + 1 is exclusive), taking steps of size 'p'
            # (which means we efficiently only visit multiples of p).
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
                
    # Now our sieve is complete. We will extract all the numbers that remain marked as True.
    # We create an empty list to collect our prime numbers.
    primes = []
    
    # We loop through all numbers from 2 up to the limit.
    # Remember, range(2, limit + 1) goes from 2 up to, but not including, limit + 1.
    for number in range(2, limit + 1):
        if is_prime[number]:
            # The 'append' method adds an element to the end of our list.
            primes.append(number)
            
    # The 'return' statement outputs the result of our function back to wherever it was called.
    return primes


# This 'if' block is a standard Python idiom. It means: "If this script is being run directly
# by the user (rather than being imported as an add-on module into another program), 
# then execute the code inside this block."
# This is how you make the sieve easy to use as a generic mathematical function elsewhere, 
# while still providing a built-in test when someone runs the file directly.
if __name__ == "__main__":
    # We pick an arbitrary limit to test our algorithm.
    N = 2000000
    sum=0
    # We call our function and store its mathematical mapping (the returned list) into 'result_primes'.
    primes = sieve_of_eratosthenes(N)
    for p in primes:
        sum += p
    # The 'print' function outputs text to the screen.
    # The 'f' before the quotes makes it an "f-string", which allows us to embed 
    # variables directly inside curly braces {}.
    print(f"The sum of the prime numbers up to {N} is: {sum}")
