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

    def __init__(self, screen, screen_width, screen_height, x, y, hero, arr_clothes, arr_received_clothes, artefacts):
        super(InfoBoard, self).__init__(screen, screen_width, screen_height, x, y, hero, 0)
        self.arr_clothes = [arr_clothes[4], arr_clothes[1], arr_clothes[3], arr_clothes[0], arr_clothes[2],
                            arr_clothes[5]]
        self.arr_received_clothes = arr_received_clothes
        y = screen_height // 2
        self.artefacts = artefacts
        self.rect = (self.x, y - 280, 280, 420)
        self.rect_items = (screen_width - 285, y - 186, 280, 372)
        self.size_cell = 140, 140
        self.size_cell_items = 93, 93
        self.flag_item = True
        self.flag_render_artifacts = False
        self.rect_artefacts = (262, 100, 700, 500)
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
        for i in range(2):
            for j in range(3):
                if self.arr_clothes[i * 3 + j] != "default":
                    color = [0, 150, 0]
                else:
                    color = [100, 100, 100]
                rect = self.rect[0] + i * 140, self.rect[1] + j * 140, \
                       self.size_cell[0], \
                       self.size_cell[1]
                pygame.draw.rect(self.screen, color, rect, width=0)
                icon = pygame.transform.scale(self.icons[i * 3 + j], (self.size_cell[0], self.size_cell[1]))
                self.screen.blit(icon, (rect[0], rect[1]))
                pygame.draw.rect(self.screen, (255, 255, 255), rect, width=1)
        myfont = pygame.font.SysFont('Liberation Serif', 50)
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect_button_inventory, width=0)
        text = myfont.render("artefacts", False, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + 150, self.screen_height - 100))
        self.screen.blit(text, text_rect)
        self.render_items()
        self.chest_render()
        if self.flag_render_artifacts:
            self.render_artefacts()

    def render_items(self):
        for i in range(3):
            for j in range(4):
                color = [100, 100, 100]
                rect = self.rect_items[0] + i * self.size_cell_items[0], \
                       self.rect_items[1] + j * self.size_cell_items[1], \
                       self.size_cell_items[0], self.size_cell_items[1]
                pygame.draw.rect(self.screen, color, rect, width=0)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, width=1)
                if not (i * 4 + j >= len(self.arr_received_clothes)):
                    name_item = self.arr_received_clothes[i * 4 + j]
                    if name_item.split()[1] == "sword":
                        icon = icons[0]
                    elif name_item.split()[1] == "body":
                        icon = icons[1]
                    elif name_item.split()[1] == "gloves":
                        icon = icons[2]
                    elif name_item.split()[1] == "greaves":
                        icon = icons[3]
                    elif name_item.split()[1] == "helmet":
                        icon = icons[4]
                    elif name_item.split()[1] == "ring":
                        icon = icons[5]
                    icon = pygame.transform.scale(icon, (self.size_cell_items[0] - 6, self.size_cell_items[1] - 6))
                    self.screen.blit(icon, (rect[0] + 3, rect[1] + 3))

    def transferring_item(self, item, pos):
        if item.split()[1] == "sword":
            icon = icons[0]
        elif item.split()[1] == "body":
            icon = icons[1]
        elif item.split()[1] == "gloves":
            icon = icons[2]
        elif item.split()[1] == "greaves":
            icon = icons[3]
        elif item.split()[1] == "helmet":
            icon = icons[4]
        elif item.split()[1] == "ring":
            icon = icons[5]
        icon = pygame.transform.scale(icon, (self.size_cell_items[0] - 6, self.size_cell_items[1] - 6))
        self.screen.blit(icon, pos)

    def equip_item(self, item):
        if item.split()[1] == "sword":
            if self.arr_clothes[3] != "default":
                self.arr_received_clothes.append(self.arr_clothes[3])
            self.arr_clothes[3] = item
        elif item.split()[1] == "body":
            if self.arr_clothes[1] != "default":
                self.arr_received_clothes.append(self.arr_clothes[1])
            self.arr_clothes[1] = item
        elif item.split()[1] == "gloves":
            if self.arr_clothes[4] != "default":
                self.arr_received_clothes.append(self.arr_clothes[4])
            self.arr_clothes[4] = item
        elif item.split()[1] == "greaves":
            if self.arr_clothes[2] != "default":
                self.arr_received_clothes.append(self.arr_clothes[2])
            self.arr_clothes[2] = item
        elif item.split()[1] == "helmet":
            if self.arr_clothes[0] != "default":
                self.arr_received_clothes.append(self.arr_clothes[0])
            self.arr_clothes[0] = item
        elif item.split()[1] == "ring":
            if self.arr_clothes[5] != "default":
                self.arr_received_clothes.append(self.arr_clothes[5])
            self.arr_clothes[5] = item
        self.arr_received_clothes.remove(item)
        f = open('ReceivedClothes.txt', mode='w')
        f.write('\n'.join(self.arr_received_clothes))
        f.close()
        arr = self.arr_clothes[3], self.arr_clothes[1], self.arr_clothes[4], self.arr_clothes[2], self.arr_clothes[0], \
              self.arr_clothes[5]
        f = open('HeroClothes.txt', mode='w')
        f.write('\n'.join(arr))
        f.close()

    def get_button(self, pos):
        x, y = pos
        if self.rect_items[1] + self.rect_items[3] >= y >= self.rect_items[1]:
            y = (y - self.rect_items[1]) // self.size_cell_items[1]
            if self.rect_items[0] + self.rect_items[2] >= x >= self.rect_items[0]:
                x = (x - self.rect_items[0]) // self.size_cell_items[0]
                return x * 4 + y
        return None

    def get_button_items(self, pos):
        x, y = pos
        if self.rect[1] + self.rect[3] >= y >= self.rect[1]:
            y = (y - self.rect[1]) // self.size_cell[1]
            if self.rect[0] + self.rect[2] >= x >= self.rect[0]:
                x = (x - self.rect[0]) // self.size_cell[0]
                return x * 3 + y
        return None

    def get_status_item(self, pos):
        x, y = pos
        if self.rect[1] + self.rect[3] >= y >= self.rect[1]:
            if self.rect[0] + self.rect[2] >= x >= self.rect[0]:
                return True
        return False

    def render_artefacts(self):
        pygame.draw.rect(self.screen, (50, 50, 50), self.rect_artefacts, width=0)
        self.window_artefact()

    def button_artefacts(self, pos):
        x, y = pos
        if self.rect_button_inventory[0] < x < self.rect_button_inventory[0] + self.rect_button_inventory[2]:
            if self.rect_button_inventory[1] < y < self.rect_button_inventory[1] + self.rect_button_inventory[3]:
                self.flag_item = not self.flag_item
                self.flag_render_artifacts = not self.flag_render_artifacts

    def window_artefact(self):
        myfont = pygame.font.SysFont('Liberation Serif', 30)
        for i in range(len(self.artefacts)):
            if i != "":
                color = [0, 150, 0]
                rect = (self.rect_artefacts[0] + 10, self.rect_artefacts[1] + ((i - 1) * 35) + 10, 700, 500)
                text = myfont.render(self.artefacts[i], False, color)
                self.screen.blit(text, (rect[0], rect[1]))

    def get_stats_item(self, pos, item):
        if item != "default" and self.flag_item:
            arr_text = []
            myfont = pygame.font.SysFont('Liberation Serif', 20)
            if item.split()[1] == "sword":
                arr_text = items_Sword[item].get_stats()
            elif item.split()[1] == "body":
                arr_text = items_BodyArmor[item].get_stats()
            elif item.split()[1] == "gloves":
                arr_text = items_Gloves[item].get_stats()
            elif item.split()[1] == "greaves":
                arr_text = items_Greaves[item].get_stats()
            elif item.split()[1] == "helmet":
                arr_text = items_Helmet[item].get_stats()
            elif item.split()[1] == "ring":
                arr_text = items_Ring[item].get_stats()
            pygame.draw.rect(self.screen, (70, 70, 70), (pos[0] - 205, pos[1] - 5, 200, 100), width=0)
            for i in range(len(arr_text)):
                text = myfont.render(arr_text[i], False, (255, 0, 0))
                rect = (pos[0] - 200, pos[1] + (i * 25))
                self.screen.blit(text, rect)

    def stats_equip_items(self, pos, flag, item):
        button = self.get_button_items(pos)
        if button != None and button < len(self.arr_clothes) and self.flag_item:
            equip_item = self.arr_clothes[button]
            if equip_item != "default":
                arr_text = []
                myfont = pygame.font.SysFont('Liberation Serif', 20)
                if equip_item.split()[1] == "sword":
                    arr_text = items_Sword[equip_item].get_stats()
                elif equip_item.split()[1] == "body":
                    arr_text = items_BodyArmor[equip_item].get_stats()
                elif equip_item.split()[1] == "gloves":
                    arr_text = items_Gloves[equip_item].get_stats()
                elif equip_item.split()[1] == "greaves":
                    arr_text = items_Greaves[equip_item].get_stats()
                elif equip_item.split()[1] == "helmet":
                    arr_text = items_Helmet[equip_item].get_stats()
                elif equip_item.split()[1] == "ring":
                    arr_text = items_Ring[equip_item].get_stats()
                if flag:
                    pygame.draw.rect(self.screen, (70, 70, 70), (pos[0] + 5, pos[1] - 100, 200, 100), width=0)
                    for i in range(len(arr_text)):
                        text = myfont.render(arr_text[i], False, (0, 255, 0))
                        rect = (pos[0] + 10, pos[1] - 95 + (i * 25))
                        self.screen.blit(text, rect)
                else:
                    pygame.draw.rect(self.screen, (70, 70, 70), (pos[0] + 5, pos[1] + 5, 200, 100), width=0)
                    for i in range(len(arr_text)):
                        text = myfont.render(arr_text[i], False, (255, 0, 0))
                        rect = (pos[0] + 10, pos[1] + 10 + (i * 25))
                        self.screen.blit(text, rect)
                if item != "" and equip_item.split()[1] == item.split()[1]:
                    self.get_stats_item((pos[0] + 210, pos[1] + 20), item)
                    self.transferring_item(item, (pos[0] - 100, pos[1]))
                    return False
        return True
