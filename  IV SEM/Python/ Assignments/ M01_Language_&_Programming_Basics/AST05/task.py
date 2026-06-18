from typing import List


def Collatz_Sequence(n: int) -> List:
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n <= 0:
        raise ValueError(f"n must be a positive integer, got {n}")
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        raise ValueError("Input must be a valid integer")
    print(Collatz_Sequence(n))