def palindrome():
    f = open('input.dat', mode='rb').read()
    return f == f[::-1]