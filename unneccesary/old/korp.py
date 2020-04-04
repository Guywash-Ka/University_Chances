a = int(input())
d = dict()
for i in range(a):
    w = input()
    ind = 0
    for j in range(len(w)):
        if w[j].isdigit() or w[j] == '@':
            ind = j
            break
    if w[:ind] in d:
        d[w[:ind]] += 1
    else:
        d[w[:ind]] = 1
for i in range(int(input())):
    w = input()
    if w in d:
        res = f'{w}{d[w]}@untitled.py'
        d[w] += 1
    else:
        res = f'{w}@untitled.py'
        d[w] = 1
    print(res)