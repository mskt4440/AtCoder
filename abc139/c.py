#
# abc139 c
#
import sys


def input():
    return sys.stdin.readline()[:-1]


def maxmove(lk, H):
    dp = {}
    dp[lk] = 0
    for i in range(lk-1, -1, -1):
        if H[i] >= H[i+1]:
            dp[i] = dp[i+1] + 1
        else:
            dp[i] = 0

    return max(dp.values())


def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(maxmove(N-1, H))


if __name__ == '__main__':
    main()
