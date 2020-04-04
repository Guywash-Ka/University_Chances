import os
import pygame
import random

size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('/home/vlad/projects/RodionPy/data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png", -1)
    image2 = load_image("boom.png", -1)
    
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(5, width - 50)
        self.rect.y = random.randrange(5, height - 51)
    
    def update(self, xy):
        x, y = xy
        if (self.rect.x < x < self.rect.x + 50) and (self.rect.y < y < self.rect.y + 50):
            self.image = Bomb.image2
    
    '''def clicked(self, xy):
        x, y = xy
        if (self.rect.x - 25 < x < self.rect.x + 25) and (self.rect.y - 25 < y < self.rect.y + 25):
            self.image = Bomb.image2'''


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
for _ in range(20):
    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event.pos)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    #all_sprites.update()
    pygame.display.flip()

pygame.quit()