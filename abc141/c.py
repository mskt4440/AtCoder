#
# abc141 c
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K, Q = map(int, input().split())
    score = [K] * N
    num = [0] * N
    ans = ["Yes"] * N
    for i in range(Q):
        i = int(input())
        num[i-1] += 1
    for i in range(N):
        score[i] -= Q - num[i]
        if score[i] <= 0:
            ans[i] = "No"

    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
