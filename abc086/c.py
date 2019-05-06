#
# abc086 c
#
n = int(input())
ret = "Yes"
for i in range(n):
    t, x, y = map(int, input().split())
    if x + y > t:
        ret = "No"
        break
    if t % 2 == 0 and (x + y) % 2 == 1:
        ret = "No"
        break
    elif t % 2 == 1 and (x + y) % 2 == 0:
        ret = "No"
        break
print(ret)
