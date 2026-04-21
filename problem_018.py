# Problem 18
# The triangle is written as a multiline string.
# Note : it works for Problem 67 as well
triangle_string = """ 75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 """

# Split the multiline string into one line per row of the triangle.
rows = triangle_string.splitlines()

# This dictionary will store the entries of the triangle.
# The keys are pairs (i, j), which are the coordinates.
triangle = {}

# We read the triangle row by row.
for r, line in enumerate(rows):
    # Split each row into its individual numbers.
    numbers = line.split()

    # Read each number together with its position inside the row.
    for c, value in enumerate(numbers):
        # We encode positions with coordinates (i, j),
        # where i = c and j = r - c.
        i = c
        j = r - c

        # Store the number as an integer.
        triangle[(i, j)] = int(value)

# print(triangle) 


def weighted_path_length(triangle, i, j, weighted_length):
    """
    Compute the maximum total from node (i, j) down to the bottom,
    using recursion + memoization.

    Parameters
    ----------
    triangle : dict
        Dictionary containing the triangle values.
    i, j : int
        Coordinates of the current node.
    weighted_length : dict
        Memoization dictionary:
        weighted_length[(i, j)] will store the best path sum
        starting from node (i, j).

    Returns
    -------
    dict
        The updated memoization dictionary.
    """

    # Memoization step:
    # if we have already computed the best path starting from (i, j),
    # do not recompute it.
    if (i, j) in weighted_length:
        return weighted_length

    # Base case:
    # if the "left child" (i+1, j) is not in the triangle,
    # then (i, j) must be in the last row.
    # So the best path starting there is just the value of that node.
    if (i + 1, j) not in triangle:
        weighted_length[(i, j)] = triangle[(i, j)]
        return weighted_length

    else:
        # Recursively compute the best path sums of the two children:
        # (i+1, j) and (i, j+1).
        weighted_path_length(triangle, i + 1, j, weighted_length)
        weighted_path_length(triangle, i, j + 1, weighted_length)

        # Once the two children are known, the best path from (i, j)
        # is its own value plus the larger of the two children's best sums.
        weighted_length[(i, j)] = triangle[(i, j)] + max(
            weighted_length[(i + 1, j)],
            weighted_length[(i, j + 1)]
        )

        return weighted_length


# Start with an empty memoization dictionary.
weighted_length = {}

# Fill it starting from the top of the triangle, at (0, 0).
weighted_length = weighted_path_length(triangle, 0, 0, weighted_length)

# The answer to the problem is the best path sum starting at the top.
print(weighted_length[(0, 0)])
