#
# abc127 c
#


def main():
    n, m = map(int, input().split())
    G = [0] * m
    ans = 0
    for i in range(m):
        G[i] = list(map(int, input().split()))
    for i in range(1, n+1):
        f = 0
        for j in range(m):
            if i < G[j][0] or G[j][1] < i:
                f = 0
                break
            else:
                f = 1
        if f == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
