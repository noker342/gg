import pygame

pygame.init()
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
x, y = 0, 0
running = True


class Cell:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.alive = False
        self.colors = [(0, 0, 0), (255, 255, 255)]

    def show(self):
        if self.alive:
            pygame.draw.rect(screen, self.colors[self.alive], (self.x, self.y, self.width, self.height))

    def dying(self):
        self.alive = not self.alive


class Background:
    def __init__(self, width, height):
        self.cells = []
        self.width = width
        self.height = height
        self.square_size = 20
        for i in range(self.height // self.square_size):
            self.cells.append([])
            for j in range(self.width // self.square_size):
                self.cells[-1].append(Cell(j * 20, i * 20, self.square_size, self.square_size))

    def draw_cells(self):
        for i in range(self.height // self.square_size):
            pygame.draw.line(screen, (255, 255, 255), (i * 20, 0), (1, 1))
            for j in range(self.width // self.square_size):
                pygame.draw.line(screen, (255, 255, 255), (0, j * 20), (1, 1))


b = Background(width, height)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    b.draw_cells()
    pygame.display.flip()
