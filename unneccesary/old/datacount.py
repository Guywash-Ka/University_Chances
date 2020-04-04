d = open('output.txt', mode='w')
with open('input.txt') as f:
    s = f.read().split()
neg = 0
pos = 0
null = 0
for i in s:
    i = int(i)
    if i < 0:
        neg += 1
    elif i > 0:
        pos += 1
    else:
        null += 1
d.write(str(len(s)) + '\n')
if pos:
    d.write(f'1 {pos} ')
if neg:
    d.write(f'-1 {neg} ')
if null:
    d.write(f'0 {null}')