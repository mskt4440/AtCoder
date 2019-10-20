#
# abc079 c
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def bitall(s):
    for bit in range(1 << 3):
        f = s[0]

        for i in range(3):
            if bit & (1 << i):
                f += "+"
                f += s[i + 1]
            else:
                f += "-"
                f += s[i + 1]

        if eval(f) == 7:
            print(f + "=7")
            exit()


def main():
    s = input()

    bitall(s)


if __name__ == '__main__':
    main()
