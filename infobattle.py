import pygame.draw
from items import items_Sword, items_BodyArmor, items_Gloves, items_Greaves, items_Ring, items_Helmet, Consumable_items

icons = [pygame.image.load("image/icons/sword.png"),
         pygame.image.load("image/icons/body_armor.png"),
         pygame.image.load("image/icons/cloves.png"),
         pygame.image.load("image/icons/creaves.png"),
         pygame.image.load("image/icons/helmet.png"),
         pygame.image.load("image/icons/ring.png")]


class Info:
    def __init__(self, screen, screen_width, screen_height, x, y, hero, enemy):
        self.arr_arr = [items_Sword, items_BodyArmor, items_Gloves, items_Greaves, items_Helmet, items_Ring]
        self.flag = -1
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size_cell = []
        self.hero = hero
        self.enemy = enemy
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, 300, 500)
        self.rect_button_inventory = (self.x, self.screen_height - 150, 300, 100)
        self.rect_inventory = (self.x + 325, round(self.screen_height * 0.7), self.screen_width - self.x - 350,
                               round(self.screen_height * 0.3))
        self.flag_inventory = False
        self.time_without_text = -1
        self.text_arr = []

    def render(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, width=1)
        myfont = pygame.font.SysFont('Liberation Serif', 50)
        for i in range(len(self.text_arr)):
            text = self.text_arr[i]
            rect = (self.x + 5, self.y + 5 + (i * 25))
            self.screen.blit(text, rect)
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect_button_inventory, width=0)
        text = myfont.render("inventory", False, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + 150, self.screen_height - 100))
        self.screen.blit(text, text_rect)
        if self.flag_inventory:
            self.render_inventory()

    def render_info(self, flag):
        myfont = pygame.font.SysFont('Liberation Serif', 20)
        if flag == 8:
            self.flag_inventory = not self.flag_inventory
        elif self.flag_inventory and 1 <= flag <= 6:
            self.text_arr = []
            hero = self.hero
            arr_str = self.arr_arr[flag - 1][hero.items[flag - 1]].get_stats()
            for i in arr_str:
                text = myfont.render(i, False, (255, 255, 255))
                self.text_arr.append(text)
        elif flag != self.flag:
            self.text_arr = []
            hero = self.hero
            enemy = self.enemy
            if flag == 1:
                dm = hero.attack(enemy, False)
                text = myfont.render("damage = " + str(dm), False, (255, 255, 255))
                self.text_arr.append(text)
                text = myfont.render("Sword:", False, (255, 255, 255))
                self.text_arr.append(text)
                arr_str = items_Sword[hero.items[0]].get_stats()
                for i in arr_str:
                    text = myfont.render(i, False, (255, 255, 255))
                    self.text_arr.append(text)
            elif flag == 2:
                hero.defense()
                text = myfont.render("defense = " + str(hero.time_def), False, (255, 255, 255))
                self.text_arr.append(text)
                dm = enemy.attack(hero, False)
                text = myfont.render("taking damage = " + str(dm), False, (255, 255, 255))
                self.text_arr.append(text)
                hero.time_def = 0
            elif flag == 3:
                heal_hp = hero.healing_hp
                text = myfont.render("healing hp = " + str(heal_hp), False, (255, 255, 255))
                self.text_arr.append(text)
                kd = hero.max_recharge_healing
                text = myfont.render("recharge healing = " + str(kd), False, (255, 255, 255))
                self.text_arr.append(text)
            elif flag == 4:
                arr = hero.get_info_consumable_item()
                name = arr[0]
                text = myfont.render("name : " + name, False, (255, 255, 255))
                self.text_arr.append(text)
                type_atk = arr[2]
                text = myfont.render("type attack : " + type_atk, False, (255, 255, 255))
                self.text_arr.append(text)
                dm = Consumable_items[name][2] * hero.atk_fire_multiplier
                text = myfont.render("damage : " + str(dm), False, (255, 255, 255))
                self.text_arr.append(text)
        self.flag = flag

    def render_inventory(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect_inventory, width=0)
        self.size_cell = ((self.rect_inventory[2] - 35) // 6, self.rect_inventory[3] - 10)
        for i in range(6):
            if self.hero.items[i] != "default":
                color = [0, 150, 0]
            else:
                color = [100, 100, 100]
            rect = self.rect_inventory[0] + (i + 1) * 5 + i * self.size_cell[0], self.rect_inventory[1] + 5, \
                   self.size_cell[0], \
                   self.size_cell[1]
            pygame.draw.rect(self.screen, color, rect, width=0)
            icon = pygame.transform.scale(icons[i], (self.size_cell[0], self.size_cell[1]))
            self.screen.blit(icon, (rect[0], rect[1]))

    def button_inventory(self, pos):
        x, y = pos
        if self.screen_width >= y >= self.rect_inventory[1]:
            if x - self.rect_inventory[0] >= 0:
                return (x - self.rect_inventory[0]) // (self.size_cell[0] + 5) + 1


class InfoBoard(Info):

    def __init__(self, screen, screen_width, screen_height, x, y, hero, arr_clothes):
        super(InfoBoard, self).__init__(screen, screen_width, screen_height, x, y, hero, 0)
        self.arr_clothes = [arr_clothes[4], arr_clothes[1], arr_clothes[3], arr_clothes[0], arr_clothes[2],
                            arr_clothes[5]]
        self.rect = (self.x, self.y, 280, 372)
        self.rect_items = (screen_width - 285, 5, 280, 560)
        self.size_cell = 140, 140
        self.size_cell_items = 93, 93
        self.icons = [pygame.image.load("image/icons/helmet.png"),
                      pygame.image.load("image/icons/body_armor.png"),
                      pygame.image.load("image/icons/creaves.png"),
                      pygame.image.load("image/icons/sword.png"),
                      pygame.image.load("image/icons/cloves.png"),
                      pygame.image.load("image/icons/ring.png")]

    def chest_render(self):
        x = self.screen_width // 2
        y = self.screen_height - 150
        for i in range(len(self.text_arr)):
            text = self.text_arr[i]
            rect = text.get_rect(center=(x, y))
            rect[1] += (i * 25)
            self.screen.blit(text, rect)
        if self.time_without_text == 0:
            self.text_arr = []
        else:
            self.time_without_text -= 1

    def without_chest_items(self, arr):
        myfont = pygame.font.SysFont('Liberation Serif', 20)
        for i in arr:
            text = myfont.render("Item received: " + i, False, (0, 255, 0))
            self.text_arr.append(text)
        self.time_without_text = 180

    def render(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, width=1)
        for i in range(2):
            for j in range(3):
                if self.arr_clothes[i * 3 + j] != "default":
                    color = [0, 150, 0]
                else:
                    color = [100, 100, 100]
                rect = self.x + i * 140, self.y + j * 140, \
                       self.size_cell[0], \
                       self.size_cell[1]
                pygame.draw.rect(self.screen, color, rect, width=0)
                icon = pygame.transform.scale(self.icons[i * 3 + j], (self.size_cell[0], self.size_cell[1]))
                self.screen.blit(icon, (rect[0], rect[1]))
                pygame.draw.rect(self.screen, (255, 255, 255), rect, width=1)
        self.render_items()
        self.chest_render()

    def render_items(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect_items, width=1)
        for i in range(3):
            for j in range(4):
                color = [100, 100, 100]
                rect = self.rect_items[0] + i * self.size_cell_items[0], \
                       self.rect_items[1] + j * self.size_cell_items[1], \
                       self.size_cell_items[0], self.size_cell_items[1]
                pygame.draw.rect(self.screen, color, rect, width=0)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, width=1)
