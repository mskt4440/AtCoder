#
# abc143 c
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    I = range(1, N+1)
    dic = dict(zip(I, A))
    dic2 = sorted(dic.items(), key=lambda x: x[1])
    ans = []
    for i in dic2:
        ans.append(i[0])
    print(*ans)


if __name__ == '__main__':
    main()
