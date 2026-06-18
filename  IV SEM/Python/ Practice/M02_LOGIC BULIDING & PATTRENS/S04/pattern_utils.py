def square_star_pattern(n):
    """Generate a square star pattern as a list of strings."""
    return ["* " * n for _ in range(n)]


def right_angle_triangle(n):
    """Generate a right-angle triangle star pattern."""
    return ["* " * (i + 1) for i in range(n)]


def reverse_right_angle_triangle(n):
    """Generate a reverse right-angle triangle star pattern."""
    return ["*" * i for i in range(n, 0, -1)]


def pyramid_pattern(n):
    """Generate a pyramid star pattern."""
    return [" " * (n - i - 1) + "*" * (2 * i + 1) for i in range(n)]
