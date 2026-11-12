"""Count the active eggs represented by a binary number."""


def egg_count(display_value):
    """Count the number of active eggs represented in a binary number.

    Args:
        display_value (int): A non-negative integer whose binary
            representation indicates which eggs are active.

    Returns:
        int: The number of set bits (1s) in ``display_value``.
    """
    eggs = 0
    while display_value:
        if display_value % 2:
            eggs += 1
        display_value //= 2
    return eggs
