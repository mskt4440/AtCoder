#
# abc085 b
#
n = int(input())
m = []

for i in range(n):
    x = int(input())
    if x not in m:
        m.append(x)
print(len(m))
