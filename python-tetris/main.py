import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 1100
WINDOW_WIDTH = 1000


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        draw_grid(500, 1000, 10, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def draw_grid(width, height, xoffset, yoffset):
    block_size = 50
    grid = []
    for x in range(0, width, block_size):
        row = []
        for y in range(0, height, block_size):
            rect = pygame.Rect(x + xoffset, y + yoffset, block_size, block_size)
            row.append([x + xoffset, y + yoffset])
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
        grid.append(row)
    # print(grid[1][1])


# def draw_tetrominoes():
#     


main()
