# Entry question
def sum_odd_squares(n):
    """Calculate the sum of the first n odd square numbers."""
    return sum((i * i) for i in range(1, 2 * n, 2))

# Main program
if __name__ == '__main__':
    n = int(input('Enter the number of odd square numbers to sum: '))
    result = sum_odd_squares(n)
    print(f'The sum of the first {n} odd square numbers is: {result}')
