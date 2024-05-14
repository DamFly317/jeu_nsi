import pygame
import sys


def draw_grid(screen):
    for x in range(screen.get_width() // CELL_SIZE):
        for y in range(screen.get_height() // CELL_SIZE):
            pygame.draw.line(
                screen,
                'white',
                (0, y * CELL_SIZE),
                (screen.get_width(), y * CELL_SIZE)
            )
            pygame.draw.line(
                screen,
                'white',
                (x * CELL_SIZE, 0),
                (x * CELL_SIZE, screen.get_height())
            )


screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption('Jeu de la vie')
CELL_SIZE = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill('black')
    draw_grid(screen)
    pygame.display.flip()
