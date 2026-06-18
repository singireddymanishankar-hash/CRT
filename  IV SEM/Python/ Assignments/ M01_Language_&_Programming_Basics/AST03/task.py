def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    if not isinstance(name, str):
        raise TypeError(f"Expected str for name, got {type(name).__name__}")
    for label, grade in [("n1", n1), ("n2", n2), ("n3", n3)]:
        if not isinstance(grade, (int, float)):
            raise TypeError(f"Expected numeric grade for {label}, got {type(grade).__name__}")
        if grade < 0 or grade > 100:
            raise ValueError(f"Grade {label} out of range (0-100): {grade}")
    average = (n1 + n2 + n3) / 3
    status = "Pass" if average >= 40 else "Fail"
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == '__main__':
    data = input()

    # Extract values from formatted input
    parts = data.replace("Name:", "").replace("Grades:", "").replace(",", "").split()

    if len(parts) < 4:
        raise ValueError(f"Expected 'Name: <name> Grades: <n1>, <n2>, <n3>', got: {data}")

    name = parts[0]
    try:
        n1, n2, n3 = map(int, parts[1:4])
    except ValueError:
        raise ValueError(f"Grades must be valid integers, got: {parts[1:4]}")

    print(Student_Grade_System(name, n1, n2, n3))