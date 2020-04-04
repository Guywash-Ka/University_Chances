import pygame
import random

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'), (j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size, self.cell_size), 1)

    def get_cell_index(self, cell_coords):
        return (cell_coords[1] - self.left) // self.cell_size, (cell_coords[0] - self.top) // self.cell_size

    def get_cell(self, mouse_pos):
        if (self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width) and (self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height):
            return (mouse_pos[0], mouse_pos[1])
        return None
    
    def on_click(self, cell_coords):
        if cell_coords:
            #print(self.get_cell_index(cell_coords))
            return self.get_cell_index(cell_coords), self.board[self.get_cell_index(cell_coords)[0]][self.get_cell_index(cell_coords)[1]]
        else:
            return None  

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.mines = mines

        self.mines_ind = random.sample([i for i in range(width * height)], mines)
        for i in range(height):
            for j in range(width):
                if width * i + j in self.mines_ind:
                    self.board[i][j] = 10
    
    def check_for_bombs(self, i, j):
        c = 0
        up = True
        down = True
        right = True
        left = True
        if i > 0:
            if self.board[i - 1][j] == 10:
                c += 1
        else:
            up = False
        if i < self.height - 1:
            if self.board[i + 1][j] == 10:
                c += 1
        else:
            down = False
        if j > 0:
            if self.board[i][j - 1] == 10:
                c += 1
        else:
            left = False
        if j < self.width - 1:
            if self.board[i][j + 1] == 10:
                c += 1
        else:
            right = False
        if up and left:
            if self.board[i - 1][j - 1] == 10:
                c += 1
        if up and right:
            if self.board[i - 1][j + 1] == 10:
                c += 1
        if down and left:
            if self.board[i + 1][j - 1] == 10:
                c += 1
        if down and right:
            if self.board[i + 1][j + 1] == 10:
                c += 1
        return c

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'), (j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                if self.board[i][j] == 10:
                    pygame.draw.rect(screen, pygame.Color('red'), (1 + j * self.cell_size + self.left, 1 + i * self.cell_size + self.top, -1 + self.cell_size, -1 + self.cell_size))
                if 0 <= self.board[i][j] < 10:
                    font = pygame.font.Font(None, 20)
                    text = font.render(str(self.board[i][j]), 1, (100, 255, 100))
                    text_x = j * 50 + 105
                    text_y = i * 50 + 105
                    text_w = text.get_width()
                    text_h = text.get_height()
                    screen.blit(text, (text_x, text_y))

    def open_cell(self, xy):
        if self.on_click(xy)[1] == -1:
            i = self.on_click(xy)[0][0]
            j = self.on_click(xy)[0][1]
            a = self.check_for_bombs(i, j)
            self.board[i][j] = a

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
board = Minesweeper(10, 7, 5)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.open_cell(event.pos)      
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()