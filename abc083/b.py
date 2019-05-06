#
# abc083 b
#
n, a, b = map(int, input().split())
ret = 0
for i in range(n+1):
    x = 0
    s = str(i)
    for j in range(len(s)):
        x += int(s[j])
    if x >= a and x <= b:
        ret += i
print(ret)
