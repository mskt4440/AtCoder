#
# abc132 b
#


def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-2):
        if p[i+1] != min(p[i:i+3]) and p[i+1] != max(p[i:i+3]):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
