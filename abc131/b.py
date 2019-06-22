#
# abc131 b
#


def main():
    N, L = map(int, input().split())
    pia = int((L + L + N - 1) * N / 2)

    eat = L
    for i in range(1, N+1):
        if abs(eat) > abs(L+i-1):
            eat = L+i-1

    print(pia - eat)


if __name__ == '__main__':
    main()
