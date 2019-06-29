#
# abc132 a
#


def main():
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        ans = "No"
    elif S[0] == S[1] and S[2] == S[3]:
        ans = "Yes"
    elif S[0] == S[2] and S[1] == S[3]:
        ans = "Yes"
    elif S[0] == S[3] and S[1] == S[2]:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == '__main__':
    main()
