#
# abc085 c
#
n, y = map(int, input().split())

flag = 0
for i in range(n+1):
    for j in range(n+1):
        if y == 10000 * i + 5000 * j + 1000 * (n-i-j) and n-i-j >= 0:
            flag = 1
        if flag == 1:
            break
    if flag == 1:
        break

if flag == 0:
    print("-1 -1 -1")
else:
    print(i, j, n-i-j)
