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


default_spawn_position = [0, 3]
playable_blocks = ['I', 'O', 'T', 'J', 'L', 'Z', 'S']
bag = []
is_placed = True
cur_block = ''
blocks_visible = 5
grid_positions = []
grid_game = []
gravity = 0.1
block_size = 50


def main():
    global SCREEN, CLOCK, grid_game, grid_positions
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    grid = init_grid(500, 1000, 50, 10)
    grid_positions = grid[0]
    grid_game = grid[1]
    tick = pygame.USEREVENT + 1
    tick_interval = 500
    pygame.time.set_timer(tick, tick_interval)

    while True:
        draw_next_position()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == tick:
                calculate_next_position()

        pygame.display.update()


def init_grid(width, height, xoffset, yoffset):
    global block_size
    _grid_positions = []
    for y in range(0, height, block_size):
        row = []
        for x in range(0, width, block_size):
            rect = pygame.Rect(x + xoffset, y + yoffset, block_size, block_size)
            row.append([x + xoffset, y + yoffset])
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
        _grid_positions.append(row)

    _grid_game = [[0 for y in x] for x in _grid_positions]
    return [_grid_positions, _grid_game]
    # print(grid_game)
    # print(grid[1][1])


def generate_bag():
    generated_bag = playable_blocks
    random.shuffle(generated_bag)
    print("bag generated")
    return generated_bag


def calculate_next_position():
    global bag, is_placed, cur_block, blocks_visible
    if len(bag) <= blocks_visible:
        [bag.append(x) for x in generate_bag()]
    if is_placed:
        cur_block = [bag[0]]
        bag.pop(0)
        is_placed = False
        spawn_next_block()
    else:
        apply_gravity()
    print(grid_game)


def apply_gravity():
    global gravity, grid_game, grid_positions, cur_block
    for i in range(len(grid_game)):
        for j in range(len(grid_game[0])):
            if grid_game[i][j] == 2:
                grid_game[i][j] = 1
                grid_game[i - 17][j] = 2
                print(i)
    # print("afdsdsa")


def spawn_next_block():
    global cur_block, default_spawn_position, grid_positions, grid_game
    cur_block_shape = [len(blocks[cur_block[0]]), len(blocks[cur_block[0]][0])]
    for i in range(cur_block_shape[0]):
        for j in range(cur_block_shape[1]):
            grid_game[i + default_spawn_position[0]][j + default_spawn_position[1]] = 2 if blocks[cur_block[0]][i][j] == 1 else 0
    print(grid_game)


def draw_next_position():
    global grid_positions, grid_game, block_size
    for i in range(len(grid_game)):
        for j in range(len(grid_game[0])):
            if grid_game[i][j] > 0:
                cur_grid_position = grid_positions[i][j]
                rect = pygame.Rect(cur_grid_position[0], cur_grid_position[1], block_size, block_size)
                pygame.draw.rect(SCREEN, (0, 0, 100), rect, 1)


main()
