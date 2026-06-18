def count_digits(n):
    """Count the number of digits in a positive integer."""
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n > 0:
        count += 1
        n = n // 10
    return count


def sum_of_digits(n):
    """Return the sum of digits of a non-negative integer."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def reverse_number(n):
    """Reverse the digits of a non-negative integer."""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev


def is_palindrome_number(n):
    """Check if a non-negative integer is a palindrome."""
    return n == reverse_number(n)
