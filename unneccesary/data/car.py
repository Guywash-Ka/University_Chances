import os
import pygame
import random

size = width, height = 600, 95
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


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png", pygame.Color('black'))
    
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно!!!
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 15
        self.right = True
    
    def update(self):
        if self.rect.x == width - 150:
            self.right = False
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.rect.x == 0:
            self.right = True
            self.image = pygame.transform.flip(self.image, True, False)
        if self.right:
            self.rect = self.rect.move(1, 0)
        else:
            self.rect = self.rect.move(-1, 0)


clock = pygame.time.Clock()

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()
Car(all_sprites)
fps = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()