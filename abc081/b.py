#
# abc081 b
#
n = int(input())
a = list(map(int, input().split()))
r = [0] * n

for i in range(n):
    while a[i] % 2 == 0:
        a[i] /= 2
        r[i] += 1

print(min(r))
