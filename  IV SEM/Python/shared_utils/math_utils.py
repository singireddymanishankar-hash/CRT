"""
Core math utilities.

Consolidates duplicated factorial, primality, and factor logic from:
- Practice/M02_.../S02/PS02_Factors&primes.py  (factorial, is_prime, factors)
- Practice/M02_.../S03/PS03_series.py           (factorial)
"""

from typing import List


def factorial(n: int) -> int:
    """Return n! (iterative)."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_factors(n: int) -> List[int]:
    """Return all factors of *n* in ascending order."""
    n = abs(n)
    factors: List[int] = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    if n != 0:
        factors.append(n)
    return factors


def count_factors(n: int) -> int:
    """Return the count of factors of *n*."""
    return len(get_factors(n))


def primes_in_range(start: int, end: int) -> List[int]:
    """Return all primes in [start, end]."""
    return [n for n in range(start, end + 1) if is_prime(n)]
