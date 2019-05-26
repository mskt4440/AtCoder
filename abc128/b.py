#
# abc128 b
#


def main():
    n = int(input())
    L = []
    for i in range(n):
        s, p = input().split()
        L.append([i, s, int(p)])

    L = sorted(L, key=lambda x: x[2], reverse=True)
    L = sorted(L, key=lambda x: x[1])
    for i in range(n):
        print(L[i][0]+1)


if __name__ == '__main__':
    main()
