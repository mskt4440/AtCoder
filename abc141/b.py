#
# abc141 b
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = input()
    ans = "Yes"
    for i in range(len(S)):
        if (i+1) % 2 == 1:
            if S[i] == "L":
                ans = "No"
        else:
            if S[i] == "R":
                ans = "No"
        if ans == "No":
            print(ans)
            exit()
    print(ans)


if __name__ == '__main__':
    main()
