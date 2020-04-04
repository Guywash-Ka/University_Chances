f = open('prices.txt')
s = 0.0
lines = f.readlines()
if lines:
    for i in lines:
        i = i.split()
        s += float(i[1]) * float(i[2])
print(s)