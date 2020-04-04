import sys

a = input()
data = list(map(str.strip, sys.stdin))
c, words = 0, []
for i in data:
    if set(i) <= set(a):
        k = True
        for j in i:
            if i.count(j) > a.count(j):
                k = False
        if k:
            c += 1
            words.append(i)
print(c)
for i in words:
    print(i)