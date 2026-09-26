def sum_range(a, b):
    # BUG: excludes b, should be inclusive per docstring below
    """Return the sum of all integers from a to b, inclusive."""
    total = 0
    for n in range(a, b + 1):
        total += n
    return total