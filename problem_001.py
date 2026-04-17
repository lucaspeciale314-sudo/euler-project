# Project Euler Problem 1 Solution
# This program computes the sum of all multiples of 3 or 5 that are less than or equal to a user-input number n.
# The mathematical approach used:
# 1. Calculate the sum of multiples of 3
# 2. Calculate the sum of multiples of 5
# 3. Subtract the sum of multiples of 15 (to avoid double-counting)

def sum_of_multiples(n):
    # Calculate the sum of multiples of k less than or equal to n
    def sum_multiples(k):
        p = (n - 1) // k  # Largest multiple of k less than n
        return k * p * (p + 1) // 2  # Sum of the first p multiples

    return sum_multiples(3) + sum_multiples(5) - sum_multiples(15)  # Combine results

if __name__ == '__main__':
    n = int(input('Enter a number: '))  # Take user input
    print(f'The sum of all multiples of 3 or 5 less than or equal to {n} is: {sum_of_multiples(n)}')  # Output the result
