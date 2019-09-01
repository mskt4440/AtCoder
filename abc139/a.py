#
# abc139 a
#
import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    S = input()
    T = input()
    ret = 0
    for i in range(3):
        if S[i] == T[i]:
            ret += 1
    print(ret)


if __name__ == '__main__':
    main()
