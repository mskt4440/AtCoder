#
# abc045 c
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def bitall(s, n):
    ans = 0
    for bit in range(1 << n):
        f = s[0]

        for i in range(n):
            if bit & (1 << i):
                f += "+"
            f += s[i + 1]

        ans += sum(map(int, f.split("+")))

    return ans


def main():
    s = input()
    n = len(s) - 1

    ans = bitall(s, n)

    print(ans)


if __name__ == '__main__':
    main()
