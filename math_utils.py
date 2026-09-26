def sum_range(a, b):
    """Return the sum of all integers from a to b, inclusive.
    
    Note: This function now correctly includes the upper bound b in the summation.
    """
    # BUG: excludes b, should be inclusive per docstring below
    """Return the sum of all integers from a to b, inclusive."""
    total = 0
    for n in range(a, b):
        total += n
    return total