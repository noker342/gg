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
        self.cells_dead = []
        self.width = width
        self.height = height
        self.square_size = 20
        for i in range(self.height // self.square_size):
            self.cells.append([])
            for j in range(self.width // self.square_size):
                self.cells[-1].append(Cell(j * 20, i * 20, self.square_size, self.square_size))

    def draw_cells(self):
        for i in range(self.height // self.square_size):
            for j in range(self.width // self.square_size):
                self.cells[i][j].show()

    def cell_count(self, x, y):
        score = 0
        if 0 <= y - 1 < 54 and 0 <= x - 1 < 96:
            if self.cells[y - 1][x - 1].alive:
                score += 1
        if 0 <= y - 1 < 54 and 0 <= x < 96:
            if self.cells[y - 1][x].alive:
                score += 1
        if 0 <= y - 1 < 54 and 0 <= x + 1 < 96:
            if self.cells[y - 1][x + 1].alive:
                score += 1
        if 0 <= y < 54 and 0 <= x - 1 < 96:
            if self.cells[y][x - 1].alive:
                score += 1
        if 0 <= y < 54 and 0 <= x + 1 < 96:
            if self.cells[y][x + 1].alive:
                score += 1
        if 0 <= y + 1 < 54 and 0 <= x - 1 < 96:
            if self.cells[y + 1][x - 1].alive:
                score += 1
        if 0 <= y + 1 < 54 and 0 <= x < 96:
            if self.cells[y + 1][x].alive:
                score += 1
        if 0 <= y + 1 < 54 and 0 <= x + 1 < 96:
            if self.cells[y + 1][x + 1].alive:
                score += 1
        return score

    def dead_cells(self):
        for i in range(self.height // self.square_size):
            self.cells_dead.append([])
            for j in range(self.width // self.square_size):
                if not b.cells[i][j].dying():
                    self.cells[-1].append(Cell(j * 20, i * 20, self.square_size, self.square_size))
        print(self.cells)

b = Background(width, height)
# b.cells[34][28].dying()
# b.cells[2][43].dying()
# b.cells[51][51].dying()
# b.cells[52][94].dying()
b.cells[53][95].dying()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    b.draw_cells()
    b.cell_count(95, 54)
    b.dead_cells()
    pygame.display.flip()