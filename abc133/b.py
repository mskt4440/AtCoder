#
# abc133 b
#
import math


def main():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))

    ans = 0
    for i in range(1, N):
        for j in range(i):
            d2 = 0
            for k in range(D):
                d2 += abs(X[i][k] - X[j][k]) ** 2
            d = math.sqrt(d2)
            if d.is_integer():
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
