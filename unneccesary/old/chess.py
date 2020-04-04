import pygame

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

        self.next_x = True

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
            x1, y1 = self.get_cell_index(cell_coords)
            if self.next_x:
                if not self.board[y1][x1]:
                    self.board[y1][x1] = 1
                    #pygame.draw.line(screen, pygame.Color('red'), (x * self.cell_size + self.left + 4, y * self.cell_size + self.top + 4), ((x + 1) * self.cell_size + self.left - 4, (y + 1) * self.cell_size + self.top - 4), 2)
                    #pygame.draw.line(screen, pygame.Color('red'),((x + 1) * self.cell_size + self.left - 4, y * self.cell_size + self.top + 4), ((x * self.cell_size + self.left + 4, (y + 1) * self.cell_size + self.top - 4)), 2)
                    self.next_x = False
            else:
                #pygame.draw.circle(screen, pygame.Color('blue'), ((x * self.cell_size + self.left) // 2, (y * self.cell_size + self.top) // 2), self.cell_size // 2)
                if not self.board[y1][x1]:
                    self.next_x = True
                    self.board[y1][x1] = 2
            for y in range(self.height):
                for x in range(self.width):
                    pygame.draw.rect(screen, pygame.Color('white'), (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)
                    if self.board[y][x] == 1:
                        pygame.draw.line(screen, pygame.Color('red'), (x * self.cell_size + self.left + 4, y * self.cell_size + self.top + 4), ((x + 1) * self.cell_size + self.left - 4, (y + 1) * self.cell_size + self.top - 4), 2)
                        pygame.draw.line(screen, pygame.Color('red'),((x + 1) * self.cell_size + self.left - 4, y * self.cell_size + self.top + 4), ((x * self.cell_size + self.left + 4, (y + 1) * self.cell_size + self.top - 4)), 2)
                    elif self.board[y][x] == 2:
                        pygame.draw.circle(screen, pygame.Color('blue'), (x * self.cell_size + (self.cell_size // 2) + self.left, y * self.cell_size + self.cell_size // 2 + self.top), self.cell_size // 2 - 4, 2)
            pygame.display.flip()
        else:
            print('None') 
                        


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
board = Board(5, 7)
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