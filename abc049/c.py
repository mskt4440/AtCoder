#
# abc049 c
#
s = input()
words = ['dream', 'dreamer', 'erase', 'eraser']

s = s[::-1]
while len(s) > 0:
    flag = 0
    for w in words:
        w = w[::-1]
        if s[0:len(w)] == w:
            s = s[len(w)::]
            flag = 1
            break
    if flag == 0:
        print("NO")
        exit()

print("YES")
