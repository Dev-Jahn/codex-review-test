"""Small collection of utility helpers."""


def average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def divide(a, b):
    """Divide a by b."""
    return a / b


def append_item(item, target=[]):
    """Append item to target and return it."""
    target.append(item)
    return target


def find_max(numbers):
    """Return the largest number in the list."""
    largest = 0
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def get_first_word(text):
    """Return the first whitespace-separated word of text."""
    return text.split(" ")[0]
