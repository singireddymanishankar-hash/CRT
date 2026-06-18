"""
Series / sequence generators.

Consolidates duplicated series logic from:
- Practice/M03_.../S01/PS01_Time complexity.py  (fibonacci recursive)
- Practice/M02_.../S03/PS03_series.py           (fibonacci, arithmetic, geometric, factorial series)
- Assignments/.../AST05/task.py                 (Collatz sequence)
"""

from typing import List

from .math_utils import factorial


def fibonacci_iterative(n: int) -> List[int]:
    """Return the first *n* Fibonacci numbers (iterative)."""
    if n <= 0:
        return []
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def fibonacci_recursive(n: int) -> int:
    """Return the *n*-th Fibonacci number (0-indexed, recursive)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def arithmetic_series(start: int, diff: int, count: int) -> List[int]:
    """Return *count* terms of an arithmetic series."""
    return [start + i * diff for i in range(count)]


def geometric_series(start: int, ratio: int, count: int) -> List[int]:
    """Return *count* terms of a geometric series."""
    return [start * (ratio ** i) for i in range(count)]


def factorial_series(n: int) -> List[int]:
    """Return [1!, 2!, ..., n!]."""
    result: List[int] = []
    running = 1
    for i in range(1, n + 1):
        running *= i
        result.append(running)
    return result


def collatz_sequence(n: int) -> List[int]:
    """Return the Collatz sequence starting from *n* down to 1."""
    sequence: List[int] = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence
