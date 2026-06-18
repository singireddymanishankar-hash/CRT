"""
Shared utilities for CRT Python practice and assignments.

This package consolidates duplicated code patterns found across
multiple practice and assignment files into reusable modules:

- digit_utils: Digit extraction, reversal, counting, summing
- math_utils: Factorial, primality, factors, GCD
- series_utils: Fibonacci, arithmetic, geometric, factorial, Collatz series
- pattern_utils: Star/number pattern printing helpers
- string_utils: String reversal, palindrome checks
"""

from .digit_utils import (
    count_digits,
    sum_of_digits,
    extract_digits,
    extract_even_digits,
    reverse_number,
    is_palindrome_number,
)
from .math_utils import (
    factorial,
    is_prime,
    get_factors,
    count_factors,
    primes_in_range,
)
from .series_utils import (
    fibonacci_iterative,
    fibonacci_recursive,
    arithmetic_series,
    geometric_series,
    factorial_series,
    collatz_sequence,
)
from .pattern_utils import (
    square_pattern,
    right_triangle_pattern,
    inverted_right_triangle_pattern,
    pyramid_pattern,
    diamond_pattern,
    number_pyramid_pattern,
    pascal_triangle_pattern,
    hollow_pyramid_pattern,
)
from .string_utils import (
    reverse_string,
    is_palindrome_string,
)
