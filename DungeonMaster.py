import pygame
import Rooms
import random
import pprint


class Room:
    def __init__(self):
        self.CellsTypes = random.choice([Rooms.Room1])
        self.Cells = []
        for i in range(len(board.board)):
            self.Cells.append([])
            for j in range(len(board.board[i])):
                self.Cells[i].append(
                    Cell(ScreenWidth // 2 + board.cell_size * j - board.cell_size * board.width // 2,
                         board.cell_size * i + 50, self[i][j]))
        self.HeroPositionCell = self.CellsTypes[3][0]
        self.CellsTypes[3][0] = 'Hero'
        self.HeroPosition = [3, 0]
        self.Cells[3][0].type = 'Hero'

    def __str__(self):
        return str(self.Cells)

    def __getitem__(self, item):
        return self.CellsTypes[item]

    def __setitem__(self, key, value):
        self.CellsTypes[key] = value


class Cell:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.visible = False

    def draw(self):
        if self.visible:
            DrawingCell = pygame.image.load(CellsDict[self.type])
        else:
            DrawingCell = pygame.image.load("image/cells/hidden_cell.png")
        screen.blit(DrawingCell, (self.x, self.y))

    def __str__(self):
        return self.type


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.cell_size = 30

    def render(self, surface, room):
        screen.fill((0, 0, 0))
        for i in range(len(self.board)):
            for j in range(len(board.board[i])):
                room.Cells[i][j].draw()
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
        j = x // self.cell_size
        i = y // self.cell_size
        if 0 <= i < self.height and 0 <= j < self.width:
            return i, j


ItemsDict = {

}
CellsDict = {
    'Empty': 'image/cells/normal_cell.png',
    'Hero': 'image/cells/hero.png',
    'Mount': 'image/cells/mount.png',
    'Enemy': 'image/cells/enemy.png',
    'Chest': 'image/cells/chest.png',
    'Potion': 'image/cells/potions.png'
}

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    size = ScreenWidth, ScreenHeight = 900, 700
    screen = pygame.display.set_mode(size)

board = Board(9, 7)
board.cell_size = ScreenHeight // 10
Room = Room()
Room.Cells[Room.HeroPosition[0]][Room.HeroPosition[1]].visible = True
Room.Cells[Room.HeroPosition[0] - 1][Room.HeroPosition[1] + 1].visible = True
Room.Cells[Room.HeroPosition[0]][Room.HeroPosition[1] + 1].visible = True
Room.Cells[Room.HeroPosition[0] + 1][Room.HeroPosition[1] + 1].visible = True
Room.Cells[Room.HeroPosition[0] - 1][Room.HeroPosition[1]].visible = True
Room.Cells[Room.HeroPosition[0] + 1][Room.HeroPosition[1]].visible = True
board.render(screen, Room)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            CellMovePosition = board.get_cell(event.pos)
            HeroX, HeroY = Room.HeroPosition[0], Room.HeroPosition[1]
            if CellMovePosition != None:
                MoveX, MoveY = CellMovePosition
                if (abs(HeroY - MoveY) == 1 and
                    MoveX == HeroX) or \
                        (abs(HeroX - MoveX) == 1 and
                         MoveY == HeroY):
                    Room.CellsTypes[HeroX][HeroY] = Room.HeroPositionCell
                    Room.Cells[HeroX][HeroY].type = Room.HeroPositionCell
                    Room.HeroPositionCell = Room.CellsTypes[MoveX][MoveY]
                    HeroX, HeroY = Room.HeroPosition = [MoveX, MoveY]
                    Room.CellsTypes[HeroX][HeroY] = 'Hero'
                    Room.Cells[HeroX][HeroY].type = 'Hero'
                    if HeroX > 0:
                        pass
                    board.render(screen, Room)
    pygame.display.flip()
