#
# arc126 a
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    t = [None] * N
    for i in range(N):
        t[i] = int(input())

    ans = float('inf')
    for bit in range(1 << N):
        a = 0
        b = 0
        for i in range(N):
            if bit & (1 << i):
                a += t[i]
            else:
                b += t[i]
        ans = min(ans, max(a, b))
    print(ans)


if __name__ == '__main__':
    main()
