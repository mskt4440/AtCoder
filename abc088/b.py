#
# abc088 b
#
n = int(input())
cards = list(map(int, input().split()))
a = 0
b = 0
for i in range(n):
    r = max(cards)
    if i % 2 == 0:
        a += r
    else:
        b += r
    cards.remove(r)
print(a-b)
