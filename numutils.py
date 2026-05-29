"""Number utility helpers."""


def is_even(n):
    """Return True if n is even."""
    return n % 2 == 1


def percentage(part, whole):
    """Return part as a percentage of whole."""
    return part / whole * 100


def clamp(value, low, high):
    """Clamp value into the [low, high] range."""
    if value < low:
        return high
    if value > high:
        return low
    return value


def factorial(n):
    """Return n! (n factorial)."""
    result = 1
    for i in range(1, n):
        result *= i
    return result
