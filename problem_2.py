"""
Sum of Fibonacci numbers F_{3k} up to a user-chosen limit.

We use the closed formula

    F_n = (a^n - b^n) / rho

where
    rho = sqrt(5)
    a = (rho + 1) / 2
    b = (1 - rho) / 2

We only consider n in the arithmetic progression
    n = 3k   with k = 1, 2, 3, ...

and we stop before the first value F_{3k} that exceeds the chosen limit.

Instead of summing term by term, we use geometric-series formulas:

    sum_{k=1}^m F_{3k}
  = (1 / rho) * [ sum_{k=1}^m (a^3)^k - sum_{k=1}^m (b^3)^k ]
"""

import math


def fibonacci_closed(n: int) -> int:
    """
    Return the Fibonacci number F_n using Binet's formula.

    Parameters
    ----------
    n : int
        The index of the Fibonacci number.

    Returns
    -------
    int
        The integer Fibonacci number F_n.

    Python notes
    ------------
    - math.sqrt(5) computes the square root of 5.
    - ** means "raise to a power", so a**n means a^n.
    - round(x) rounds x to the nearest integer.
    - int(...) converts the result into an integer type.

    We round because floating-point arithmetic may produce values like
    143.99999999999997 instead of exactly 144.
    """
    rho = math.sqrt(5)
    a = (rho + 1) / 2
    b = (1 - rho) / 2

    return int(round((a**n - b**n) / rho))


def geometric_sum(r: float, m: int) -> float:
    """
    Compute the finite geometric sum

        r + r^2 + ... + r^m

    Parameters
    ----------
    r : float
        The common ratio.
    m : int
        The number of terms.

    Returns
    -------
    float
        The value of the sum.

    Formula used
    ------------
        r + r^2 + ... + r^m = r * (r^m - 1) / (r - 1)

    Python notes
    ------------
    - A function is defined with def.
    - The arrow -> float is a type hint: it tells the reader that this
      function is expected to return a float.
    - return sends the computed value back to the caller.
    """
    return r * (r**m - 1) / (r - 1)


def largest_valid_k(limit: int) -> int:
    """
    Find the largest integer k >= 1 such that F_{3k} <= limit.

    Parameters
    ----------
    limit : int
        The maximum allowed Fibonacci value.

    Returns
    -------
    int
        The largest valid k.

    Python notes
    ------------
    - while True: creates an indefinite loop.
    - break would exit a loop immediately.
    - here we instead use return as soon as the answer is known.
    """
    k = 1

    while True:
        current_value = fibonacci_closed(3 * k)

        if current_value > limit:
            return k - 1

        k += 1


def sum_fibonacci_3k_closed(limit: int) -> tuple[int, int]:
    """
    Compute the sum

        F_3 + F_6 + F_9 + ... + F_{3m}

    where m is the largest integer such that F_{3m} <= limit.

    Parameters
    ----------
    limit : int
        The upper bound.

    Returns
    -------
    tuple[int, int]
        A pair (m, total_sum), where:
        - m is the largest valid k,
        - total_sum is the sum of F_{3k} for k = 1, ..., m.

    Python notes
    ------------
    - tuple[int, int] means the function returns two integers packed together.
    - You can unpack them later with syntax like:
          m, total = sum_fibonacci_3k_closed(limit)
    """
    rho = math.sqrt(5)
    a = (rho + 1) / 2
    b = (1 - rho) / 2

    m = largest_valid_k(limit)

    r1 = a**3
    r2 = b**3

    sum1 = geometric_sum(r1, m)
    sum2 = geometric_sum(r2, m)

    total = (sum1 - sum2) / rho

    return m, int(round(total))


def sum_fibonacci_3k_direct(limit: int) -> int:
    """
    Compute the same sum directly term by term.

    This is not the main method requested, but it is useful as a check
    that the geometric-series computation is correct.
    """
    total = 0
    k = 1

    while True:
        value = fibonacci_closed(3 * k)

        if value > limit:
            break

        total += value
        k += 1

    return total


def main() -> None:
    """
    Main entry point of the program.

    This function:
    1. asks the user for the limit,
    2. computes the sum using the closed formula,
    3. checks it with the direct method,
    4. prints the results.

    Python notes
    ------------
    - input(...) displays a message and waits for the user to type something.
    - input always returns a string, so we convert it with int(...).
    - print(...) displays text on the screen.
    - f"..." is an f-string: it lets us insert values inside text using { }.
    """
    limit = int(input("Enter the upper limit: "))

    m, closed_sum = sum_fibonacci_3k_closed(limit)
    direct_sum = sum_fibonacci_3k_direct(limit)

    print()
    print(f"Largest k such that F_(3k) <= {limit}: k = {m}")

    if m >= 1:
        print(f"Last included term: F_{3*m} = {fibonacci_closed(3*m)}")
        print(f"Next term: F_{3*(m+1)} = {fibonacci_closed(3*(m+1))} (excluded)")
    else:
        print("No term F_{3k} is small enough to be included.")

    print(f"Sum using geometric-series closed formula: {closed_sum}")
    print(f"Sum by direct verification:              {direct_sum}")
    print(f"Results agree: {closed_sum == direct_sum}")


if __name__ == "__main__":
    main()
