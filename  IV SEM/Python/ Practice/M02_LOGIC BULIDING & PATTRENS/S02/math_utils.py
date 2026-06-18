def get_factors(n):
    """Return a sorted list of all factors of a positive integer n."""
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors


def count_factors(n):
    """Return the number of factors of a positive integer n."""
    return len(get_factors(n))


def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Return a list of all prime numbers in the range [start, end]."""
    return [n for n in range(start, end + 1) if is_prime(n)]


def factorial(num):
    """Return the factorial of a non-negative integer."""
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
