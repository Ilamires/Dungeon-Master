import pygame
import Rooms
import random


class Room:
    def __init__(self):
        self.set_Room()
        self.Cells = []

    def __str__(self):
        return str(self.Cells)

    def __getitem__(self, item):
        return self.CellsTypes[item]

    def __setitem__(self, key, value):
        self.CellsTypes[key] = value

    def set_Room(self):
        self.CellsTypes = random.choice([Rooms.Room1])


class Cell:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.visible = False

    def set_Visible(self, visible):
        self.visible = visible
        self.draw()

    def draw(self):
        if self.visible:
            if self.type == 'Stone':
                DrawingCell = pygame.image.load("image/mount.png")
            elif self.type == 'Enemy':
                DrawingCell = pygame.image.load("image/enemy.png")
            elif self.type == 'Chest':
                DrawingCell = pygame.image.load("image/chest.png")
            elif self.type == 'Potion':
                DrawingCell = pygame.image.load("image/potions.png")
            else:
                DrawingCell = pygame.image.load("image/normal_cell.png")
        else:
            DrawingCell = pygame.image.load("image/hidden_cell.png")
        screen.blit(DrawingCell, (self.x, self.y))
        pygame.display.update()

    def __str__(self):
        return self.type


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.cell_size = 30

    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self, surface, room):
        for i in range(len(self.board)):
            room.Cells.append([])
            for j in range(len(self.board[i])):
                room.Cells[i].append(
                    Cell(ScreenWidth // 2 + self.cell_size * j - self.cell_size * self.width // 2,
                         self.cell_size * i + 50, room[i][j]))
                room.Cells[i][j].set_Visible(False)
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


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size = ScreenWidth, ScreenHeight = 900, 700
    screen = pygame.display.set_mode(size)

board = Board(9, 7)
board.set_view(ScreenHeight // 10)
screen.fill((0, 0, 0))
Room1 = Room()
board.render(screen, Room1)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board.get_cell(event.pos))
    pygame.display.flip()
