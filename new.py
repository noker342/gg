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
        self.true = True
        self.color = (255, 255, 255)

    def show(self):
        if self.true:
            pygame.draw.rect(screen, self.color, (20, 20, 40, 40))

    def dying(self):


c = Cell(x, y, width, height)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    c.show()
    pygame.display.flip()
