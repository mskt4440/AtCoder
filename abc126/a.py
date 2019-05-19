#
# abc126 a
#


def main():
    n, k = map(int, input().split())
    s = input()
    print(s[0:k-1] + s[k-1:k].lower() + s[k:])


if __name__ == '__main__':
    main()
