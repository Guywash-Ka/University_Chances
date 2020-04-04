a, b = input(), int(input())
if abs(b) >= len(a):
    b = b % len(a)
first_str = a[b:] + a[:b]
third_str = a[-b:] + a[:-b]    
print(first_str, a, third_str, sep='\n')