a = input().split(' -> ')
for i in range(int(input())):
    name = input()
    ind = a.index(name)
    if ind == 0:
        print(name, a[ind + 1], sep=' -> ')
    elif ind == len(a) - 1:
        print(a[ind - 1], name, sep=' -> ')
    else:
        print(a[ind - 1], name, a[ind + 1], sep=' -> ')