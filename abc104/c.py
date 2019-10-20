#
# abc104 c
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    D, G = map(int, input().split())
    problems = [[None] * 2 for _ in range(D)]
    ans = float('inf')

    for i in range(D):
        problems[i] = list(map(int, input().split()))

    for bit in range(1 << D):
        score = 0
        solved = 0
        unsolved = set(range(D))
        for j in range(D):
            if bit & (1 << j):
                score += problems[j][0] * (j+1) * 100 + problems[j][1]
                solved += problems[j][0]
                unsolved.discard(j)

        if score < G:
            use = max(unsolved)
            n = min(problems[use][0]-1, -
                    (-(G - score) // ((use + 1) * 100)))  # 繰り上げ
            score += n * (use + 1) * 100
            solved += n

        if score >= G:
            ans = min(ans, solved)

    print(ans)


if __name__ == '__main__':
    main()
