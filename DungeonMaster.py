import pygame
import Rooms
import random


class Room:
    def __init__(self):
        self.set_Rooms()

    def __str__(self):
        return str(self.Cells)

    def __getitem__(self, item):
        return self.Cells[item]

    def __setitem__(self, key, value):
        self.Cells[key] = value

    def set_Rooms(self):
        self.Cells = random.choice(Rooms.Rooms)


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.cell_size = 30

    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self, surface):
        Cells = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                Cells.append(Cell(j, i))
                pygame.draw.rect(surface, (255, 255, 255),
                                 (ScreenWidth // 2 + self.cell_size * j - self.cell_size * self.width // 2,
                                  self.cell_size * i + 50,
                                  self.cell_size,
                                  self.cell_size), 1)

    def get_cell(self, pos):
        x0 = ScreenWidth // 2 - self.cell_size * self.width // 2
        y0 = 50
        x = pos[0] - x0
        y = pos[1] - y0
        j = x // self.cell_size + 1
        i = y // self.cell_size + 1
        if 1 <= i < self.height + 1 and 1 <= j < self.width + 1:
            return j, i
        else:
            return None


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size = ScreenWidth, ScreenHeight = 900, 700
    screen = pygame.display.set_mode(size)

running = True
board = Board(9, 7)
board.set_view(ScreenHeight // 10)
screen.fill((0, 0, 0))
board.render(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board.get_cell(event.pos))
    pygame.display.flip()
