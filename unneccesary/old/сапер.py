import pygame

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
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
        return (cell_coords[0] - self.left) // self.cell_size, (cell_coords[1] - self.top) // self.cell_size

    def get_cell(self, mouse_pos):
        if (self.left <= mouse_pos[0] <= self.left + self.cell_size * self.width) and (self.top <= mouse_pos[1] <= self.top + self.cell_size * self.height):
            return (mouse_pos[0], mouse_pos[1])
        return None
    
    def on_click(self, cell_coords):
        if cell_coords:
            x, y = self.get_cell_index(cell_coords)
            print(x, y)
            print(self.board)
            self.board[y][x] += 1
            if self.board[y][x] == 3:
                self.board[y][x] = 0
            for i in range(self.height):
                for j in range(self.width):
                    if not self.board[i][j]:
                        pygame.draw.rect(screen, pygame.Color('white'), (j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                    elif self.board[i][j] == 1:
                        pygame.draw.rect(screen, pygame.Color('red'), (j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size, self.cell_size))
                    elif self.board[i][j] == 2:
                        pygame.draw.rect(screen, pygame.Color('blue'), (j * self.cell_size + self.left, i * self.cell_size + self.top, self.cell_size, self.cell_size))
            pygame.display.flip()
        else:
            print('None') 
                        


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
board = Board(10, 31)
board.set_view(100, 100, 50)
running = True
board.render()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos) 
            pygame.display.flip()          
    screen.fill((0, 0, 0))