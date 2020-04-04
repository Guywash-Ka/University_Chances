import os
import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):
    fullname = os.path.join('/home/vlad/projects/RodionPy/data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


clock = pygame.time.Clock()

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

# изображение должно лежать в папке data
cursor_image = load_image("car2.png")
cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()
pygame.transform.flip(cursor_image, True, True)

# скрываем системный курсор
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # изменяем положение спрайта-стрелки
                cursor.rect.top -= 10
            elif event.key == pygame.K_DOWN:
                # изменяем положение спрайта-стрелки
                cursor.rect.top += 10
            elif event.key == pygame.K_LEFT:
                # изменяем положение спрайта-стрелки
                cursor.rect.left -= 10
            elif event.key == pygame.K_RIGHT:
                # изменяем положение спрайта-стрелки
                cursor.rect.left += 10
    screen.fill(pygame.Color("white"))
    # рисуем курсор только если он в пределах окна
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()