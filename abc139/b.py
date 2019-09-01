#
# abc139 b
#
import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    A, B = map(int, input().split())
    if B == 1:
        print("0")
        exit()
    else:
        for i in range(1, 100):
            if (A-1)*(i-1) + A >= B:
                print(i)
                exit()


if __name__ == '__main__':
    main()
