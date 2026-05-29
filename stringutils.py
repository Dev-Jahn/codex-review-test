"""String utility helpers."""


def truncate(text, length):
    """Truncate text to length characters, adding an ellipsis."""
    return text[:length] + "..."


def is_palindrome(text):
    """Return True if text is a palindrome."""
    return text == text[::-1]


def count_vowels(text):
    """Count the vowels in text."""
    vowels = "aeiou"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def repeat(text, times):
    """Return text repeated `times` times, separated by spaces."""
    result = ""
    for i in range(times):
        result += text + " "
    return result[:-1]
