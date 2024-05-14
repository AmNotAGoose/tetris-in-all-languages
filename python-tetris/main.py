import pygame
import sys
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 1100
WINDOW_WIDTH = 1000

blocks = {
    'I': [
      [1,1,1,1]
    ],
    'J': [
      [1,0,0],
      [1,1,1]
    ],
    'L': [
      [0,0,1],
      [1,1,1]
    ],
    'O': [
      [1,1],
      [1,1],
    ],
    'S': [
      [0,1,1],
      [1,1,0]
    ],
    'Z': [
      [1,1,0],
      [0,1,1]
    ],
    'T': [
      [0,1,0],
      [1,1,1]
    ]
  }

grid_positions = []
grid_game = []

cur_block = []
is_placed = True
bag = []

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    init_grid(500, 1000, 10, 10)
    while True:
        calculate_next_position()
        draw_next_position()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def init_grid(width, height, xoffset, yoffset):
    block_size = 50
    grid_positions = []
    for x in range(0, width, block_size):
        row = []
        for y in range(0, height, block_size):
            rect = pygame.Rect(x + xoffset, y + yoffset, block_size, block_size)
            row.append([x + xoffset, y + yoffset])
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
        grid_positions.append(row)

    grid_game = [[0 for y in x] for x in grid_positions]
    # print(grid_game)
    # print(grid[1][1])


def generate_bag():


def calculate_next_position():
    if is_placed:


def draw_next_position():


main()
