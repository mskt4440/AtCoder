#
# abc131 a
#


def main():
    S = input()
    ans = "Good"
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans = "Bad"
            break
    print(ans)


if __name__ == '__main__':
    main()
