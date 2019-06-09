#
# abc129 b
#


def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = sum(w)
    for i in range(n):
        w1 = []
        w2 = []
        for j in range(n):
            if j <= i:
                w1.append(w[j])
            else:
                w2.append(w[j])
        tmp = abs(sum(w1) - sum(w2))
        if tmp < ans:
            ans = tmp
    print(ans)


if __name__ == '__main__':
    main()
