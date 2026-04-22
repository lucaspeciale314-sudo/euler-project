# Problem 66: Diophantine equation
# We use the fact that the minimal solution to x^2 - D*y^2 = 1
# can be computed using the continued fraction of sqrt(D)

import math

def continued_fraction_sqrt(c: int) -> tuple[int, tuple[int, ...]]:
    """
    Compute the continued fraction of sqrt(c) using integer arithmetic.
    Returns (a0, (a1, a2, ..., am)) where the second element is the periodic part.
    For perfect squares, the period is empty.
    Credit to Wiikipedia page
    """
    a0 = math.isqrt(c)

    # Perfect square
    if a0 * a0 == c:
        return (a0, ())

    m, d, a = 0, 1, a0
    period = []
    seen = set()

    while True:
        m = d * a - m
        d = (c - m * m) // d
        a = (a0 + m) // d

        if (m, d, a) in seen:
            break

        seen.add((m, d, a))
        period.append(a)

    return (a0, tuple(period))


def compute_approximant(cf, m):
    """
    Compute the m-th convergent of the continued fraction.
    m = 0 gives [a0]
    m = 1 gives [a0; a1]
    m = 2 gives [a0; a1, a2], etc.
    For periodic continued fractions, the period is repeated as needed.
    """
    a0, period = cf

    if not period:
        return [a0, 1]

    # Build the list of coefficients a_0, ..., a_m
    terms = [a0]
    for i in range(m):
        terms.append(period[i % len(period)])

    # Standard recurrence for convergents
    p_minus_2, p_minus_1 = 0, 1
    q_minus_2, q_minus_1 = 1, 0

    for a in terms:
        p = a * p_minus_1 + p_minus_2
        q = a * q_minus_1 + q_minus_2
        p_minus_2, p_minus_1 = p_minus_1, p
        q_minus_2, q_minus_1 = q_minus_1, q

    return [p_minus_1, q_minus_1]


#continued_fraction = continued_fraction_sqrt(2)
#A = compute_approximant(continued_fraction, 111)
#print(A)
biggest_numerator=1
it=0
for D in range(2,1000):
    cf=continued_fraction_sqrt(D)
    period=cf[1]
    if len(period) == 0:
        continue
    if len(period)%2 == 0:
        num=compute_approximant(cf,len(period)-1)[0]
    else: num=compute_approximant(cf,2*len(period)-1)[0]
        
    if num > biggest_numerator:
        biggest_numerator=num
        it=D
print(it)
