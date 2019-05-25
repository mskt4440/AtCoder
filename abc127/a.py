#
# abc127 a
#


def main():
    ret = 0
    a, b = map(int, input().split())
    if a <= 5:
        ret = 0
    elif a <= 12:
        ret = b // 2
    else:
        ret = b
    print(ret)


if __name__ == '__main__':
    main()
