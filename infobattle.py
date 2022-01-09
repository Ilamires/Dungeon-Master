import pygame.draw
from items import items_Sword, Consumable_items


class Info:
    def __init__(self, screen, screen_width, screen_height, x, y, hero, enemy):
        self.flag = -1
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hero = hero
        self.enemy = enemy
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, 300, 500)
        self.rect_button_inventory = (self.x, self.screen_height - 150, 300, 100)
        self.rect_inventory = (self.x + 325, round(self.screen_height * 0.7), self.screen_width - self.x - 350,
                               round(self.screen_height * 0.3))
        self.flag_inventory = False
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
        if flag == 5:
            self.flag_inventory = not self.flag_inventory
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
        size_cell = ((self.rect_inventory[2] - 35) // 6, self.rect_inventory[3] - 10)
        for i in range(6):
            if self.hero.items[i] != "default":
                color = [0, 150, 0]
            else:
                color = [100, 100, 100]
            rect = self.rect_inventory[0] + (i + 1) * 5 + i * size_cell[0], self.rect_inventory[1] + 5, size_cell[0], \
                   size_cell[1]
            pygame.draw.rect(self.screen, color, rect, width=0)
