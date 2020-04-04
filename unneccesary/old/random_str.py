from random import randint

f = open('lines.txt')
lines = f.readlines()
if lines:
    print(lines[randint(0, len(lines) - 1)])