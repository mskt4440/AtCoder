#
# abc127 c
#


def main():
    n, m = map(int, input().split())
    l = []
    r = []
    ans = 0
    for i in range(m):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    ml = max(l)
    mr = min(r)
    for i in range(1, n+1):
        if i >= ml and i <= mr:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
