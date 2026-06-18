def Ticket_Pricing(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"Age cannot be negative: {n}")
    if n < 5:
        return 0
    elif n <= 17:
        return 10
    elif n <= 64:
        return 20
    else:
        return 15


if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        raise ValueError("Input must be a valid integer")
    print(Ticket_Pricing(n))