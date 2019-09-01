#
# abc139 d
#
import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N = int(input())
    ret = 0
    for i in range(1, N):
        ret += i
    print(ret)


if __name__ == '__main__':
    main()
