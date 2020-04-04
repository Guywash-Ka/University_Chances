import sys

data = list(map(str.strip, sys.stdin))
c = 0
words = ['далек', 'далеки', 'далека', 'далеков',
         'далеку', 'далекам', 'далеком', 'далеками', 'далеке', 'далеках']
for i in data:
    i = i.lower()
    for j in i.split():
        if j in words:
            c += 1
            break
print(c)