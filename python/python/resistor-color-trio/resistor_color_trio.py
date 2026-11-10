"""Utilities for translating resistor color bands into a human-readable label."""

COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]


def label(colors):
    """Return the resistance value described by a three-band resistor color code.

    The first two colors represent significant digits, and the third color
    represents the multiplier power of ten. The result is formatted with an
    appropriate suffix such as ohms, kiloohms, megaohms, or gigaohms.

    :param colors: A list of three color names matching the resistor bands.
    :return: A string containing the calculated resistance value and unit.
    """
    resistance = (COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10 ** COLORS.index(colors[2])
    unit = "ohms"
    if resistance < 1000:
        return f"{resistance} {unit}"
    if resistance < 1000000:
        return f"{resistance // 1000} kilo{unit}"
    if resistance < 1000000000:
        return f"{resistance // 1000000} mega{unit}"
    return f"{resistance // 1000000000} giga{unit}"