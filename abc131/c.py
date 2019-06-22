#
# abc131 c
#


def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x


def main():
    A, B, C, D = map(int, input().split())
    R = int(C * D / gcd(C, D))

    tmp = B // C - (A-1) // C + B // D - (A-1) // D - B // R + (A-1) // R
    print(B-A+1-tmp)


if __name__ == '__main__':
    main()
