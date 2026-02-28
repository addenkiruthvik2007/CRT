def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3
    avg_rounded = round(avg, 2)

    # Status based on average
    status = "Pass" if avg_rounded >= 50 else "fail"

    return f"Average grade: {avg_rounded}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))