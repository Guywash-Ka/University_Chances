import sys

data = list(map(str.strip, sys.stdin))
c = 0
for i in data:
    i = i.lower()
    for j in i.split():
        if 'далек' == j[:5]:
            c += 1
            break
print(c)