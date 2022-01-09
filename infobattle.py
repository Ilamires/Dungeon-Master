import pygame.draw
from items import items_Sword, Consumable_items


class Info:
    def __init__(self, screen, x, y):
        self.flag = -1
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, 300, 500)
        self.text_arr = []

    def render(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, width=1)
        for i in range(len(self.text_arr)):
            text = self.text_arr[i]
            rect = (self.x + 5, self.y + 5 + (i * 25))
            self.screen.blit(text, rect)

    def render_info(self, hero, other, flag, ):
        myfont = pygame.font.SysFont('Liberation Serif', 20)
        if flag != self.flag:
            self.text_arr = []
            if flag == 1:
                dm = hero.attack(other)
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
                dm = other.attack(hero)
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
            elif flag == 5:
                pass
        self.flag = flag
