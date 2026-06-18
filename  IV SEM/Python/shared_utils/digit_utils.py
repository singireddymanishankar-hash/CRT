"""
Digit manipulation utilities.

Consolidates the repeated n % 10 / n //= 10 loop pattern found in
Practice/M02_.../S01/PS01_Digits_problems.py (count, sum, extract, reverse)
and the palindrome check in Practice/M02_.../S03/PS04_Number_validation.py.
"""

from typing import List


def count_digits(n: int) -> int:
    """Return the number of digits in *n*."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def sum_of_digits(n: int) -> int:
    """Return the sum of all digits of *n*."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def extract_digits(n: int) -> List[int]:
    """Return a list of digits of *n* in original (left-to-right) order."""
    n = abs(n)
    if n == 0:
        return [0]
    digits: List[int] = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    return digits


def extract_even_digits(n: int) -> List[int]:
    """Return even digits of *n* in left-to-right order."""
    return [d for d in extract_digits(n) if d % 2 == 0]


def reverse_number(n: int) -> int:
    """Return *n* with its digits reversed."""
    negative = n < 0
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return -rev if negative else rev


def is_palindrome_number(n: int) -> bool:
    """Return True if *n* reads the same forwards and backwards."""
    return n == reverse_number(n)
