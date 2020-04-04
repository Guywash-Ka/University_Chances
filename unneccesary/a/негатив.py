with open("input.bmp", "rb") as f:
    b = f.read()
    li = [*b[:54]]
    for i in range(54, len(b)):
        li.append(255 - b[i])


with open("res.bmp", "wb") as f:
    f.write(bytes(li))