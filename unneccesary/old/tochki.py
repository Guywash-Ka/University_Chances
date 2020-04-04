a = dict()
for i in range(int(input())):
    x, y = input().split()
    x, y = int(x), int(y)
    if y < abs(x) and y > -abs(x):
        print(f'({x}, {y})')
    if 'left' in a:
        if a['left'][0] > x:
            a['left'] = (x, y)
    else:
        a['left'] = (x, y)
    if 'right' in a:
        if a['right'][0] < x:
            a['right'] = (x, y)
    else:
        a['right'] = (x, y)
    if 'top' in a:
        if a['top'][1] < y:
            a['top'] = (x, y)
    else:
        a['top'] = (x, y)
    if 'bottom' in a:
        if a['bottom'][1] > y:
            a['bottom'] = (x, y)
    else:
        a['bottom'] = (x, y)
for i in a:
    print(f'{i}: {a[i]}')