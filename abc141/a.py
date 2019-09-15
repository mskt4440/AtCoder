#
# abc141 a
#
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = input()
    if S == "Sunny":
        print("Cloudy")
    elif S == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")


if __name__ == '__main__':
    main()
