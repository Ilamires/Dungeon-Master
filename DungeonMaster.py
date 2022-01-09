import pygame
import Rooms
import random
import sys
from items import items_Artefacts
from battle import start_battle
from MainMenu import start_mainmenu


def start_map():
    class Room:
        def __init__(self):
            self.CreateNewRoom()

        def set_Coords(self):
            for i in range(len(board.board)):
                for j in range(len(board.board[i])):
                    self.Cells[i][j].x = ScreenWidth // 2 + board.cell_size * j \
                                         - board.cell_size * board.width // 2
                    self.Cells[i][j].y = board.cell_size * i + 50

        def CreateNewRoom(self):
            if not Continue:
                self.CellsTypes = random.choice([Rooms.CreateRooms()[0]])
            else:
                f = open("Map.txt", mode="r")
                self.CellsTypes = f.read().split('\n')
                f.close()
                f = open("MapVisible.txt", mode="r")
                Positions = f.read().split('\n')
                f.close()
                for i in range(len(self.CellsTypes)):
                    self.CellsTypes[i] = self.CellsTypes[i].split()
                    Positions[i] = Positions[i].split()
            self.Cells = []
            for i in range(len(board.board)):
                self.Cells.append([])
                for j in range(len(board.board[i])):
                    if self.CellsTypes[i][j] == 'Chest':
                        self.Cells[i].append(Chest(j, i))
                    else:
                        self.Cells[i].append(Cell(j, i, self.CellsTypes[i][j]))
                    if Continue:
                        if Positions[i][j] == '1':
                            self.Cells[i][j].visible = True

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
            if not Continue:
                self.item = Artefacts.pop()
            else:
                for i in range(len(board.board)):
                    for j in range(len(board.board[i])):
                        if ItemsInChest[i][j] != '0' and j == x and i == y:
                            self.item = ItemsInChest[i][j]

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
            if not Continue:
                self.OpenMap(self.HeroPosition[0], self.HeroPosition[1])

        def CorrectPosition(self):
            self.x = ScreenWidth // 2 + board.cell_size * self.HeroPosition[1] \
                     - board.cell_size * board.width // 2
            self.y = board.cell_size * self.HeroPosition[0] + 50
            DrawingCell = pygame.image.load("image/cells/hero.png")
            DrawingCell = pygame.transform.scale(DrawingCell, (board.cell_size, board.cell_size))
            screen.blit(DrawingCell, (self.x, self.y))

        def OpenMap(self, HeroX, HeroY):
            Room.Cells[HeroX][HeroY].visible = True
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
            if 'Lantern' in Received_artefacts or 'Torch' in Received_artefacts:
                if HeroY < 7:
                    Room.Cells[HeroX][HeroY + 2].visible = True
                    if HeroX > 1:
                        Room.Cells[HeroX - 2][HeroY + 2].visible = True
                        Room.Cells[HeroX - 2][HeroY + 1].visible = True
                    if HeroX > 0:
                        Room.Cells[HeroX - 1][HeroY + 2].visible = True
                    if HeroX < 6:
                        Room.Cells[HeroX + 1][HeroY + 2].visible = True
                    if HeroX < 5:
                        Room.Cells[HeroX + 2][HeroY + 2].visible = True
                        Room.Cells[HeroX + 2][HeroY + 1].visible = True
                elif HeroY < 8:
                    if HeroX > 1:
                        Room.Cells[HeroX - 2][HeroY + 1].visible = True
                    if HeroX < 5:
                        Room.Cells[HeroX + 2][HeroY + 1].visible = True
                if HeroY > 1:
                    Room.Cells[HeroX][HeroY - 2].visible = True
                    if HeroX > 1:
                        Room.Cells[HeroX - 2][HeroY - 2].visible = True
                        Room.Cells[HeroX - 2][HeroY - 1].visible = True
                    if HeroX > 0:
                        Room.Cells[HeroX - 1][HeroY - 2].visible = True
                    if HeroX < 6:
                        Room.Cells[HeroX + 1][HeroY - 2].visible = True
                    if HeroX < 5:
                        Room.Cells[HeroX + 2][HeroY - 2].visible = True
                        Room.Cells[HeroX + 2][HeroY - 1].visible = True
                elif HeroY > 0:
                    if HeroX > 1:
                        Room.Cells[HeroX - 2][HeroY - 1].visible = True
                    if HeroX < 5:
                        Room.Cells[HeroX + 2][HeroY - 1].visible = True
                if HeroX > 1:
                    Room.Cells[HeroX - 2][HeroY].visible = True
                if HeroX < 5:
                    Room.Cells[HeroX + 2][HeroY].visible = True

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

    def Save():
        l = []
        n = []
        m = []
        for i in range(len(Room.CellsTypes)):
            n.append([])
            l.append([])
            m.append(' '.join(Room.CellsTypes[i]))
            for j in range(len(Room.CellsTypes[i])):
                if Room.Cells[i][j].type == 'Chest':
                    l[i].append(Room.Cells[i][j].item)
                else:
                    l[i].append('0')
                if Room.Cells[i][j].visible:
                    n[i].append('1')
                else:
                    n[i].append('0')
            n[i] = ' '.join(n[i])
            l[i] = '/'.join(l[i])
        n = '\n'.join(n)
        m = '\n'.join(m)
        l = '\n'.join(l)
        f = open("MapVisible.txt", mode="w")
        f.write(n)
        f.close()
        f = open("Map.txt", mode="w")
        f.write(m)
        f.close()
        f = open("HeroPosition.txt", mode="w")
        f.write(' '.join(list(map(str, Hero.HeroPosition))))
        f.close()
        f = open("ReceivedArtefacts.txt", mode="w")
        f.write('/'.join(Received_artefacts))
        f.close()
        f = open("Artefacts.txt", mode="w")
        f.write('/'.join(Artefacts))
        f.close()
        f = open("ItemsInChest.txt", mode="w")
        f.write(l)
        f.close()
        f = open("MapNumber.txt", mode="w")
        f.write(str(NumberOfRooms) + ' ' + str(RoomNumber))
        f.close()

    Received_artefacts = []
    NumberOfRooms = 5
    RoomNumber = 1
    CellsDict = {
        'Empty': 'image/cells/normal_cell.png',
        'Hero': 'image/cells/hero.png',
        'Mount': 'image/cells/mount.png',
        'Enemy': 'image/cells/enemy.png',
        'Chest': 'image/cells/chest.png',
        'Exit': 'image/cells/potions.png',
        'Potion': 'image/cells/potions.png'
    }

    f = open('Continue.txt', mode='r')
    Continue = bool(int(f.read()))
    f.close()
    HeroPos = [3, 0]
    Artefacts = list(items_Artefacts.keys())

    if Continue:
        f = open('HeroPosition.txt', mode='r')
        HeroPos = list(map(int, f.read().split()))
        f.close()
        f = open('ReceivedArtefacts.txt', mode='r')
        Received_artefacts = f.read().split("/")
        f.close()
        f = open('Artefacts.txt', mode='r')
        Artefacts = f.read().split("/")
        f.close()
        f = open('ItemsInChest.txt', mode='r')
        ItemsInChest = f.read().split("\n")
        for i in range(len(ItemsInChest)):
            ItemsInChest[i] = ItemsInChest[i].split('/')
        f.close()
        f = open('MapNumber.txt', mode='r')
        NumberOfRooms, RoomNumber = list(map(int, f.read().split()))
        f.close()
        f = open('Continue.txt', mode='w')
        f.write('0')
        f.close()

    f = open('Fullscreen.txt', mode='r')
    Fullscreen = bool(int(f.read()))
    f.close()
    pygame.init()
    pygame.display.set_caption('Dungeon Master')
    if Fullscreen:
        size = ScreenWidth, ScreenHeight = pygame.display.Info().current_w, \
                                           pygame.display.Info().current_h
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    else:
        size = ScreenWidth, ScreenHeight = 900, 700
        screen = pygame.display.set_mode(size)

    hero_sprite = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    board = Board(9, 7)
    board.cell_size = ScreenHeight // 10
    Room = Room()
    Hero = Hero(*HeroPos)

    all_sprites.update()
    all_sprites.draw(screen)
    hero_sprite.update([0, 0])
    hero_sprite.draw(screen)
    board.render(screen)
    running = True
    clock = pygame.time.Clock()
    Continue = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Save()
                f = open('Continue.txt', mode='w')
                f.write('0')
                f.close()
                sys.exit()
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
                        Hero.OpenMap(HeroX, HeroY)
                        if Room.CellsTypes[MoveX][MoveY] == 'Chest':
                            Room.CellsTypes[MoveX][MoveY] = 'Empty'
                            Room.Cells[MoveX][MoveY].type = 'Empty'
                            Received_artefacts.append(Room.Cells[MoveX][MoveY].item)
                            Hero.OpenMap(HeroX, HeroY)
                        if Room.CellsTypes[MoveX][MoveY] == 'Potion':
                            Room.CellsTypes[MoveX][MoveY] = 'Empty'
                            Room.Cells[MoveX][MoveY].type = 'Empty'
                        if Room.CellsTypes[MoveX][MoveY] == 'Enemy':
                            Room.CellsTypes[MoveX][MoveY] = 'Empty'
                            Room.Cells[MoveX][MoveY].type = 'Empty'
                            Save()
                            pygame.quit()
                            start_battle()
                        if Room.CellsTypes[MoveX][MoveY] == 'Exit':
                            RoomNumber += 1
                            if RoomNumber == NumberOfRooms:
                                Save()
                                pygame.quit()
                                start_battle()
                            else:
                                for i in range(len(board.board)):
                                    for j in range(len(board.board[i])):
                                        Room.Cells[i][j].kill()
                                Hero.HeroPosition = [3, 0]
                                Hero.CorrectPosition()
                                Room.CreateNewRoom()
                                for i in range(len(board.board)):
                                    for j in range(len(board.board[i])):
                                        Room.Cells[i][j].visible = False
                                Hero.OpenMap(*Hero.HeroPosition)
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
                        f = open('Fullscreen.txt', mode='w')
                        f.write('1')
                        f.close()
                    else:
                        size = ScreenWidth, ScreenHeight = 900, 700
                        screen = pygame.display.set_mode(size)
                        f = open('Fullscreen.txt', mode='w')
                        f.write('0')
                        f.close()
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
start_mainmenu()

