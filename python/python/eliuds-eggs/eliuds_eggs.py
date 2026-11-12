"""Count the active eggs represented by a binary number."""
from math import ceil, log2
def egg_count(display_value):
    """Count the number of active eggs represented in a binary number.
 
    Args:
        display_value (int): A non-negative integer whose binary
            representation indicates which eggs are active.
 
    Returns:
        int: The number of set bits (1s) in ``display_value``.
    """
    digits = ceil(log2(display_value + 1))
    eggs = 0
    for digit in range(digits):
        mask = 1 << digit
        if display_value & mask:
            eggs += 1
    return eggs