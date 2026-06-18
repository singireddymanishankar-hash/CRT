def pascal_triangle_row(row_index):
    """Generate a single row of Pascal's triangle (0-indexed)."""
    row = []
    c = 1
    for j in range(row_index + 1):
        row.append(c)
        c = c * (row_index - j) // (j + 1)
    return row


def pascal_triangle(n):
    """Generate the first n rows of Pascal's triangle."""
    return [pascal_triangle_row(i) for i in range(n)]
