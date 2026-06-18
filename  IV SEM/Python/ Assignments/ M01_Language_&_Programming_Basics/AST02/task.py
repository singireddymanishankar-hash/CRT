'''
'''
def even_odd(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n <= 0:
        raise ValueError(f"n must be a positive integer: {n}")
    if n % 2 != 0:
        return "Weird"
    else:
        if 2 <= n <= 5:
            return "Not Weird"
        elif 6 <= n <= 20:
            return "Weird"
        else:
            return "Not Weird"


if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        raise ValueError("Input must be a valid integer")
    print(even_odd(n))