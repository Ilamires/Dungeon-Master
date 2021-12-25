import pygame
import random
from items import Consumable_items, items_sword, items_BodyArmor


class Unit:
    def __init__(self, lv, filename, x, y, *group):
        self.anim = AnimatedSprite(filename, x, y, *group)
        self.image = self.anim.image

        self.max_hp = 100 + (lv * 0.25) * 100
        self.hp = 100 + (lv * 0.25) * 100
        self.recharge_healing = 0

        self.atk = 10 + (lv * 0.25) * 10
        self.chance_of_miss = 0

        self.protect = 4 + (lv * 0.25) * 4
        self.dop_protect = 0

        self.time_def = 0

        self.Consumable_items = ""
        self.recharge_Consumable_items = 0

        self.items = ["default", "default", "default", "default", "default", "default", "default"]

    def update(self):
        self.anim.update()

    def attack(self, other):
        flag_miss = False
        if self.chance_of_miss != 0:
            chance = random.randint(0, 100)
            if chance <= self.chance_of_miss:
                flag_miss = True
        if not flag_miss:
            if self.items[0] != "default":
                dm = items_sword[self.items[0]].attack(self, other)
            else:
                dm = items_sword[self.items[0]].attack(self, other)
            return dm

    def use_consumable_items(self):
        if self.recharge_Consumable_items == 0:
            name = self.Consumable_items
            type = Consumable_items[name][0]
            if type == "damage":
                dm = Consumable_items[name][1]
                self.recharge_Consumable_items = Consumable_items[name][2]
                return dm

    def putting_on_clothes(self, arr):
        for i in range(len(arr)):
            if arr[i] == "default":
                self.items[i] = arr[i]
        self.dop_protect = items_BodyArmor[self.items[1]].protect

    def putting_on_consumable_items(self, name):
        self.Consumable_items = name

    def taking_damage(self, dm):
        self.hp -= dm
        if self.hp < 0:
            self.hp = 0

    def defense(self):
        self.time_def = items_BodyArmor[self.items[1]].defense(self)

    def healing(self, healing_hp):
        if self.recharge_healing == 0:
            self.heal(healing_hp)
            self.recharge_healing = 5

    def heal(self, heal_hp):
        self.hp += heal_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp

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
