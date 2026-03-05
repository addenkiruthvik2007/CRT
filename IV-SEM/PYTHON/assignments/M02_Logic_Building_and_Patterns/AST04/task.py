def Reverse_String(s: str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str   # build reverse manually
    return reversed_str


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))