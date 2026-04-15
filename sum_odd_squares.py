def sum_odd_squares(n):
    """Calculate the sum of the first n odd square numbers."""
    return sum((i * i) for i in range(1, 2 * n, 2))

# Example usage
if __name__ == '__main__':
    n = 5  # Change this value to sum the first n odd square numbers
    result = sum_odd_squares(n)
    print(f'The sum of the first {n} odd square numbers is: {result}')