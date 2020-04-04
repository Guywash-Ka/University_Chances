import csv

ways = {}

with open("input.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for i, row in enumerate(reader):
        if row[2] == '':
            start, end = row[:2]
        elif row[0] not in ways:
            ways[row[0]] = {row[1]: int(row[2])}
        else:
            ways[row[0]][row[1]] = int(row[2])

minn = -1
out = []
for key, value in ways[start].items():
    if key == end:
        if minn == -1 or value < minn:
            minn = value
            transition = None
    if key not in ways:
        continue
    for k, v in ways[key].items():
        if k == end:
            if minn == -1 or v + value < minn:
                minn = v + value
                transition = key

if not transition:
    print(start, end)
else:
    print(start, transition, end)