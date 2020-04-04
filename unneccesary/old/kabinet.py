from collections import OrderedDict
import sys

rooms = dict()
data = list(map(str.strip, sys.stdin))
for i in data:
    if i:
        i = i.split()
        sub = ' '.join(i[:-1])
        if i[-1].isdigit():
            i[-1] = int(i[-1])
            if i[-1] in rooms:
                if sub not in rooms[i[-1]]:
                    rooms[i[-1]].append(sub)
            else:
                rooms[i[-1]] = [sub]
# rooms = OrderedDict(sorted(rooms.items(), key=lambda t: t[0]))
list_keys = list(rooms.keys())
list_keys.sort()
for i in list_keys:
    print(f'{i}: ', end='')
    res = ''
    for j in rooms[i]:
        res += j + ', '
    print(res[:-2])