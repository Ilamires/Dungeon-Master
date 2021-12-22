import pygame
import Rooms
import random


class Room:
    def __init__(self):
        self.CellsTypes = random.choice([Rooms.Room1])
        self.Cells = []
        for i in range(len(board.board)):
            self.Cells.append([])
            for j in range(len(board.board[i])):
                if self.CellsTypes[i][j] == 'Chest':
                    self.Cells[i].append(Chest(j, i))
                else:
                    self.Cells[i].append(Cell(j, i, self.CellsTypes[i][j]))

    def set_Coords(self):
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                self.Cells[i][j].x = ScreenWidth // 2 + board.cell_size * j \
                                     - board.cell_size * board.width // 2
                self.Cells[i][j].y = board.cell_size * i + 50


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.type = type
        self.visible = False
        self.image = pygame.Surface((board.cell_size, board.cell_size),
                                    pygame.SRCALPHA, 32)
        DrawingCell = pygame.image.load("image/cells/hidden_cell.png")
        DrawingCell = pygame.transform.scale(DrawingCell, (board.cell_size, board.cell_size))
        screen.blit(DrawingCell, (ScreenWidth // 2 - board.cell_size * board.width // 2,
                                  board.cell_size * 3 + 50))
        self.rect = pygame.Rect(x, y, board.cell_size, board.cell_size)

    def update(self):
        if self.visible:
            DrawingCell = pygame.image.load(CellsDict[self.type])
        else:
            DrawingCell = pygame.image.load("image/cells/hidden_cell.png")
        DrawingCell = pygame.transform.scale(DrawingCell, (board.cell_size, board.cell_size))
        screen.blit(DrawingCell, (ScreenWidth // 2 + board.cell_size * self.x
                                  - board.cell_size * board.width // 2,
                                  board.cell_size * self.y + 50))


class Chest(Cell):
    def __init__(self, x, y):
        super().__init__(x, y, 'Chest')
        self.item = random.choice([0])


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(hero_sprite)
        self.HeroPosition = [x, y]
        self.x = ScreenWidth // 2 + board.cell_size * self.HeroPosition[1] \
                 - board.cell_size * board.width // 2
        self.y = board.cell_size * self.HeroPosition[0] + 50
        self.image = pygame.Surface((board.cell_size, board.cell_size),
                                    pygame.SRCALPHA, 32)
        DrawingCell = pygame.image.load("image/cells/hero.png")
        DrawingCell = pygame.transform.scale(DrawingCell, (board.cell_size, board.cell_size))
        screen.blit(DrawingCell, (self.x, self.y))
        self.rect = pygame.Rect(x, y, board.cell_size, board.cell_size)

    def CorrectPosition(self):
        self.x = ScreenWidth // 2 + board.cell_size * self.HeroPosition[1] \
                 - board.cell_size * board.width // 2
        self.y = board.cell_size * self.HeroPosition[0] + 50
        DrawingCell = pygame.image.load("image/cells/hero.png")
        DrawingCell = pygame.transform.scale(DrawingCell, (board.cell_size, board.cell_size))
        screen.blit(DrawingCell, (self.x, self.y))

    def update(self, ChangePosition):
        DrawingCell = pygame.image.load("image/cells/hero.png")
        DrawingCell = pygame.transform.scale(DrawingCell, (board.cell_size, board.cell_size))
        self.x += ChangePosition[1]
        self.y += ChangePosition[0]
        screen.blit(DrawingCell, (self.x, self.y))


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.cell_size = 30

    def render(self, surface):
        for i in range(len(self.board)):
            for j in range(len(board.board[i])):
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
hero_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
board = Board(9, 7)
board.cell_size = ScreenHeight // 10
Room = Room()
Hero = Hero(3, 0)
x, y = Hero.HeroPosition[0], Hero.HeroPosition[1]
Room.Cells[x][y].visible = True
Room.Cells[x - 1][y + 1].visible = True
Room.Cells[x][y + 1].visible = True
Room.Cells[x + 1][y + 1].visible = True
Room.Cells[x - 1][y].visible = True
Room.Cells[x + 1][y].visible = True
all_sprites.update()
all_sprites.draw(screen)
hero_sprite.update([0, 0])
hero_sprite.draw(screen)
board.render(screen)
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            CellMovePosition = board.get_cell(event.pos)
            HeroX, HeroY = Hero.HeroPosition[0], Hero.HeroPosition[1]
            if CellMovePosition != None:
                MoveX, MoveY = CellMovePosition
                DifferenceX = HeroX - MoveX
                DifferenceY = HeroY - MoveY
                if ((abs(DifferenceY) == 1 and
                     MoveX == HeroX) or (abs(DifferenceX) == 1 and
                                         MoveY == HeroY)) and Room.CellsTypes[MoveX][MoveY] != 'Mount':
                    for i in range(board.cell_size // 5):
                        all_sprites.update()
                        all_sprites.draw(screen)
                        board.render(screen)
                        hero_sprite.update([-DifferenceX * 5, -DifferenceY * 5])
                        hero_sprite.draw(screen)
                        pygame.display.flip()
                        clock.tick(60)
                    Hero.HeroPosition = [Hero.HeroPosition[0] - DifferenceX,
                                         Hero.HeroPosition[1] - DifferenceY]
                    Hero.CorrectPosition()
                    HeroX, HeroY = Hero.HeroPosition[0], Hero.HeroPosition[1]

                    if Room.CellsTypes[MoveX][MoveY] == 'Chest':
                        Room.CellsTypes[MoveX][MoveY] = 'Empty'
                        Room.Cells[MoveX][MoveY].type = 'Empty'
                    if Room.CellsTypes[MoveX][MoveY] == 'Potion':
                        Room.CellsTypes[MoveX][MoveY] = 'Empty'
                        Room.Cells[MoveX][MoveY].type = 'Empty'
                    if HeroY < 8:
                        Room.Cells[HeroX][HeroY + 1].visible = True
                        if HeroX > 0:
                            Room.Cells[HeroX - 1][HeroY + 1].visible = True
                        if HeroX < 6:
                            Room.Cells[HeroX + 1][HeroY + 1].visible = True
                    if HeroY > 0:
                        Room.Cells[HeroX][HeroY - 1].visible = True
                        if HeroX > 0:
                            Room.Cells[HeroX - 1][HeroY - 1].visible = True
                        if HeroX < 6:
                            Room.Cells[HeroX + 1][HeroY - 1].visible = True
                    if HeroX > 0:
                        Room.Cells[HeroX - 1][HeroY].visible = True
                    if HeroX < 6:
                        Room.Cells[HeroX + 1][HeroY].visible = True
                    all_sprites.update()
                    all_sprites.draw(screen)
                    hero_sprite.update([0, 0])
                    hero_sprite.draw(screen)
                    board.render(screen)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                DisplaySize = pygame.display.get_window_size()
                pygame.quit()
                pygame.init()
                pygame.display.set_caption('Dungeon Master')
                if DisplaySize == (900, 700):
                    size = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                                       pygame.display.Info().current_h
                    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
                else:
                    size = ScreenWidth, ScreenHeight = 900, 700
                    screen = pygame.display.set_mode(size)
                board.cell_size = ScreenHeight // 10
                Hero.x = ScreenWidth // 2 + board.cell_size * Hero.HeroPosition[1] \
                         - board.cell_size * board.width // 2
                Hero.y = board.cell_size * Hero.HeroPosition[0] + 50
                all_sprites.update()
                all_sprites.draw(screen)
                hero_sprite.update([0, 0])
                hero_sprite.draw(screen)
                board.render(screen)
    pygame.display.flip()
    clock.tick(60)
