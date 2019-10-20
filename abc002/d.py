#
# abc002 d
#
import sys
import itertools


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    friend = [[0] * N for _ in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        friend[x-1][y-1] = 1
        friend[y-1][x-1] = 1

    ans = 0
    for bit in range(1 << N):
        group = []
        for i in range(N):
            if bit & (1 << i):
                group.append(i)

        flag = True
        for i in itertools.combinations(group, 2):
            if friend[i[0]][i[1]] == 0:
                flag = False
                break

        if flag:
            ans = max(ans, len(group))

    print(ans)


if __name__ == '__main__':
    main()
