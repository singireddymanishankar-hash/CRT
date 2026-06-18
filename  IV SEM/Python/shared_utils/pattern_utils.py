"""
Pattern-printing utilities.

Consolidates duplicated space-padding + character-printing logic from:
- Practice/M02_.../S04/PS05 Basic_patterns.py    (square, right triangle, inverted, pyramid)
- Practice/M02_.../S05/PS06_intermediate_patterns.py  (diamond, number pyramid, hollow pyramid)
- Practice/M02_.../S06/PS07_Advanced_patterns.py  (Pascal triangle)
"""

from typing import List


def square_pattern(n: int, char: str = "*") -> List[str]:
    """Return an n x n square pattern."""
    return [(" ".join([char] * n)) for _ in range(n)]


def right_triangle_pattern(n: int, char: str = "*") -> List[str]:
    """Return a right-angle triangle (row i has i+1 chars)."""
    return [" ".join([char] * (i + 1)) for i in range(n)]


def inverted_right_triangle_pattern(n: int, char: str = "*") -> List[str]:
    """Return an inverted right-angle triangle."""
    return [char * i for i in range(n, 0, -1)]


def pyramid_pattern(n: int, char: str = "*") -> List[str]:
    """Return a centered pyramid."""
    return [
        " " * (n - i - 1) + char * (2 * i + 1)
        for i in range(n)
    ]


def diamond_pattern(n: int, char: str = "*") -> List[str]:
    """Return a diamond (pyramid + inverted pyramid)."""
    lines: List[str] = []
    for i in range(1, n + 1):
        lines.append(" " * (n - i) + (char + " ") * i)
    for i in range(n - 1, 0, -1):
        lines.append(" " * (n - i) + (char + " ") * i)
    return lines


def number_pyramid_pattern(n: int) -> List[str]:
    """Return a number pyramid where row i contains 1..i."""
    lines: List[str] = []
    for i in range(1, n + 1):
        padding = " " * (n - i)
        nums = " ".join(str(j) for j in range(1, i + 1))
        lines.append(padding + " " + nums)
    return lines


def hollow_pyramid_pattern(n: int, char: str = "*") -> List[str]:
    """Return a hollow pyramid pattern."""
    lines: List[str] = []
    for i in range(n):
        if i == 0:
            lines.append(" " * (n - 1) + char)
        elif i == n - 1:
            lines.append(char * (2 * n - 1))
        else:
            spaces_outside = " " * (n - i - 1)
            spaces_inside = " " * (2 * i - 1)
            lines.append(spaces_outside + char + spaces_inside + char)
    return lines


def pascal_triangle_pattern(n: int) -> List[str]:
    """Return Pascal's triangle as a list of formatted strings."""
    lines: List[str] = []
    for i in range(n):
        padding = " " * (n - i - 1)
        c = 1
        nums: List[str] = []
        for j in range(i + 1):
            nums.append(str(c))
            c = c * (i - j) // (j + 1)
        lines.append(padding + " " + " ".join(nums))
    return lines


def print_pattern(lines: List[str]) -> None:
    """Print a pattern (list of strings) line by line."""
    for line in lines:
        print(line)
