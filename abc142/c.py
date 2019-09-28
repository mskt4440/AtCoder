#
# abc143 c
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [None] * N
    for i in range(N):
        ans[A[i]-1] = i+1
    print(*ans)


if __name__ == '__main__':
    main()
