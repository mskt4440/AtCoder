#
# abc142 a
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N == 1:
        print("1")
    elif N % 2 == 0:
        print(1 / 2)
    else:
        print(((N-1)/2 + 1) / N)


if __name__ == '__main__':
    main()
