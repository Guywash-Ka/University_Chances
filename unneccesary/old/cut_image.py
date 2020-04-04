from PIL import Image

im = Image.open('image.bmp')
w, h = im.size
for i in range(4):
    for j in range(4):
        new_im = im.crop((w // 4 * j, h // 4 * i, w // 4 * (j + 1) - 1, h // 4 * (i + 1) - 1))
        if i == 3 and j == 3:
            break
        new_im.save(f'image{i + 1}{j + 1}.bmp')