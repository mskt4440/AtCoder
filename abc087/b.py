#
# abc087 b
#
a = int(input())
b = int(input())
c = int(input())
x = int(input())

ret = 0
for i in range(a+1):
    if (i * 500) > x:
        break
    for j in range(b+1):
        if (i * 500) + (j * 100) > x:
            break
        if (i * 500) + (j * 100) + (c * 50) >= x:
            ret += 1

print(ret)
