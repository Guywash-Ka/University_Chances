import sys

str_data = sys.stdin.read().lower()
pov = set()
vopr = set()
voskl = set()
res = ''
for i in range(len(str_data)):
    a = str_data[i]
    if a not in '.?!':
        res += a
    elif a == '.':
        for j in res.split():
            pov.add(j)
        res = ''
    elif a == '?':
        for j in res.split():
            vopr.add(j)
        res = ''
    elif a == '!':
        for j in res.split():
            voskl.add(j)
        res = ''
res = []
for i in pov:
    if i in vopr and i not in voskl:
        res.append(i)
res.sort()
print(*res)