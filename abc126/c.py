#
# abc126 c
#
import math


def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        s = i
        if 1 <= s <= k-1:
            ans += 1/n * (0.5)**math.ceil(math.log2(k/s))
        else:
            ans += 1/n
    print(ans)


if __name__ == '__main__':
    main()
