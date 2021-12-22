import pygame

from items import Consumable_items


class Unit:
    def __init__(self, lv, filename, x, y, *group):
        self.anim = AnimatedSprite(filename, x, y, *group)
        self.image = self.anim.image

        self.max_hp = 100 + (lv * 0.25) * 100
        self.hp = 100 + (lv * 0.25) * 100
        self.recharge_healing = 0

        self.atk = 10 + (lv * 0.25) * 10
        self.dop_atk = 0

        self.protect = 4 + (lv * 0.25) * 4
        self.dop_protect = 0

        self.time_def = 0

        self.Consumable_items = "fireball"
        self.recharge_Consumable_items = 0
        self.items = [0, 0, 0, 0, 0, 0]

    def update(self):
        self.anim.update()

    def attack(self, other):
        if other.time_def == 0:
            dm = (self.atk + self.dop_atk) - (other.protect + other.dop_protect)
        else:
            dm = (self.atk + self.dop_atk) - other.time_def
        other.time_def = 0
        if dm < 0.2 * (self.atk + self.dop_atk):
            return 0.2 * (self.atk + self.dop_atk)
        else:
            return dm

    def use_consumable_items(self):
        if self.recharge_Consumable_items == 0:
            name = self.Consumable_items
            type = Consumable_items[name][0]
            if type == "damage":
                dm = Consumable_items[name][1]
                self.recharge_Consumable_items = Consumable_items[name][2]
                return dm

    def taking_damage(self, dm):
        self.hp -= dm
        if self.hp < 0:
            self.hp = 0

    def defense(self):
        self.time_def = (self.protect + self.dop_protect) * 2

    def healing(self, healing_hp):
        if self.recharge_healing == 0:
            self.hp += healing_hp
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            self.recharge_healing = 5

    def status(self):
        if self.hp == 0:
            return False
        else:
            return True

    def time_motion(self):
        if self.recharge_healing != 0:
            self.recharge_healing -= 1
        if self.recharge_Consumable_items != 0:
            self.recharge_Consumable_items -= 1


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, *group):
        super().__init__(*group)
        self.frames = []
        for i in filename:
            self.frames.append(pygame.image.load(i))
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
