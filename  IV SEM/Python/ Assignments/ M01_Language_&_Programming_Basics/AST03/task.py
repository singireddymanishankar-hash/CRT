def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    average = (n1 + n2 + n3) / 3
    status = "Pass" if average >= 40 else "Fail"
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == '__main__':
    try:
        data = input()
        parts = data.replace("Name:", "").replace("Grades:", "").replace(",", "").split()
        name = parts[0]
        n1, n2, n3 = map(int, parts[1:])
        print(Student_Grade_System(name, n1, n2, n3))
    except (ValueError, IndexError):
        print("Invalid input: expected format 'Name: <name> Grades: <n1>, <n2>, <n3>'")