def arithmetic_series(start, diff, count=10):
    """Generate an arithmetic series."""
    return [start + i * diff for i in range(count)]


def geometric_series(start, ratio, count=10):
    """Generate a geometric series."""
    return [start * (ratio ** i) for i in range(count)]


def fibonacci_series(n):
    """Generate the first n terms of the Fibonacci series."""
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def factorial_series(n):
    """Generate the factorial series: 1!, 2!, 3!, ..., n!"""
    result = []
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        result.append(fact)
    return result


def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]
