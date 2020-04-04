def reverse():
    f = open('input.dat', mode='rb').read()
    d = open('output.dat', mode='wb')
    d.write(f[::-1])