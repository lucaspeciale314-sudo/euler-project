# This program looks for palindromic products among 3-digit numbers
# starting from 999 down to 901.
#
# It first tries:
#   999 * 999, 999 * 998, 999 * 997, ..., 999 * 901
# If it finds a palindrome, it prints it.
# Otherwise it continues with:
#   998 * 998, 998 * 997, ..., 998 * 901
# and so on.
# NOT OPTIMAL, IT DOES NOT FIND THE LARGEST PRODUCT NECESSARILY BUT IT SO HAPPENS TO WORK HERE.

def is_palindrome(n):
    """Return True if the integer n reads the same forwards and backwards."""
    s = str(n)
    return s == s[::-1]


found = False

for a in range(999, 900, -1):          # a = 999, 998, ..., 901
    for b in range(a, 900, -1):        # b = a, a-1, ..., 901
        product = a * b

        if is_palindrome(product):
            print("Palindrome found:", product)
            print("It comes from:", a, "*", b)
            found = True
            break

    if found:
        break

if not found:
    print("No palindrome found.")
