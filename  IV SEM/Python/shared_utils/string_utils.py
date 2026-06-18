"""
String utilities.

Consolidates duplicated string-reversal / palindrome logic from:
- Assignments/.../AST04/task.py                       (reverse string)
- Practice/M02_.../S03/PS04_Number_validation.py      (palindrome via slicing)
"""


def reverse_string(s: str) -> str:
    """Return *s* reversed, character by character."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def is_palindrome_string(s: str) -> bool:
    """Return True if *s* reads the same forwards and backwards."""
    return s == s[::-1]
