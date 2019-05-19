#
# abc126 b
#


def main():
    s = input()
    a = int(s[:2])
    b = int(s[2:])
    if b == 0:
        if a > 12 or a == 0:
            print("NA")
        else:
            print("MMYY")
    elif b > 12:
        if a > 12 or a == 0:
            print("NA")
        else:
            print("MMYY")
    else:
        if a > 12 or a == 0:
            print("YYMM")
        else:
            print("AMBIGUOUS")


if __name__ == '__main__':
    main()
