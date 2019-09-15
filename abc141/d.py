#
# abc141 d
#
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] *= -1
    heapq.heapify(A)

    for i in range(M):
        maxa = -1 * heapq.heappop(A)
        if maxa == 0:
            print("0")
            exit()
        heapq.heappush(A,  maxa // 2 * (-1))
    print(sum(A) * (-1))


if __name__ == '__main__':
    main()
