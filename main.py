import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10)  # Color for background
COLOR_GRID = (40, 40, 40)  # Color for grid
COLOR_DIE_NEXT = (170, 0, 0)  # Color for next dying square
COLOR_ALIVE_NEXT = (0, 255, 0)  # Color for alive squares
COLOR_ALIVE = (255, 255, 255)


def update(screen, cells, size, withProgress=False):
    updatedCells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1 : row + 2, col - 1 : col + 2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
        if withProgress:
            if cells[row, col] == 1:
                # If cell is deserted or overpopulated cell dies
                if alive < 2 or alive > 3:
                    color = COLOR_DIE_NEXT
                # If cell has enough cells around it lives
                elif 2 <= alive <= 3:
                    updatedCells[row, col] = 1
                    color = COLOR_ALIVE
            else:
                if alive == 3:
                    updatedCells[row, col] = 1
                    color = COLOR_ALIVE_NEXT
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    return updatedCells


def main():
    # cTime = 0
    # pTime = 0
    pygame.init()
    screen = pygame.display.set_mode((1350, 1050))  # Window size
    # Filling window with cells. Background is actually COLOR_GRID so when we fill it with black there will be grids.
    cells = np.zeros((70, 90))
    screen.fill(COLOR_GRID)
    update(screen, cells, 15)

    pygame.display.flip()
    pygame.display.update()

    running = False
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 15)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                # Finding mouse position
                cells[pos[1] // 15, pos[0] // 15] = 1
                update(screen, cells, 15)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 15, withProgress=True)
            pygame.display.update()
        time.sleep(0.0001)
        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime
        # print(fps)


if __name__ == "__main__":
    main()
