#
# abc131 d
#


def main():
    N = int(input())
    jobs = []
    for i in range(N):
        job = list(map(int, input().split()))
        jobs.append(job)
    jobs.sort(key=lambda x: x[1])

    total = 0
    for job in jobs:
        total += job[0]
        if total > job[1]:
            ans = "No"
            break
    else:
        ans = "Yes"
    print(ans)


if __name__ == '__main__':
    main()
