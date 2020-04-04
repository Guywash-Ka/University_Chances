d = dict()
for i in range(int(input())):
    a = input().split()
    d[' '.join(a[:-1])] = int(a[-1])
a = input()
a = input().split()
summ = 0
summa = 0
i = 1
while a != ['.']:
    if a:
        summ += int(a[-1]) * d[' '.join(a[:-1])]
    elif a == [] or a == ['.']:
        if summ > 0:
            print(f'{i}) {summ}')
            summa += summ
            summ = 0
            i += 1
    a = input().split()
if summ > 0:
    print(f'{i}) {summ}')
    summa += summ
    summ = 0
    i += 1
print(f'Итого: {summa}')