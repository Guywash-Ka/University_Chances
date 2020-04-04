a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
for i in a:
    i = int(i)
for i in b:
    i = int(i)
a.sort()
b.sort()
for i in a:
    for j in b:
        if sum(map(int, list(str(i)))) != sum(map(int, list(str(j)))):
            i, j = str(i), str(j)
            if len(i) == 1:
                i = '0' + i
            if len(j) == 1:
                j = '0' + j
            print(i, j, sep=':')