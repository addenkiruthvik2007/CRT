def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    # Truncate to 2 decimals (NOT round)
    avg_trunc = int(avg * 100) / 100

    # Pass / fail
    status = "Pass" if avg_trunc >= 50 else "fail"

    # Formatting exactly as tests expect
    if avg_trunc.is_integer():
        avg_str = f"{avg_trunc:.1f}"   # e.g., 50.0
    else:
        avg_str = f"{avg_trunc:.2f}"   # e.g., 18.66

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == "__main__":
    name = input()
    n1, n2, n3 = map(int, input().split())
    print(Student_Grade_System(name, n1, n2, n3))