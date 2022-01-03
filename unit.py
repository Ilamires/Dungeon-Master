import pygame
import random
from items import Consumable_items, items_Sword, items_BodyArmor, items_Gloves, items_Greaves, items_Ring, items_Helmet


class Unit:
    def __init__(self, lv, filename, x, y, character, *group):
        self.anim = AnimatedSprite(filename, x, y, character, *group)
        self.image = self.anim.image

        self.dop_hp = 0
        self.hp = 100 + (lv * 0.25) * 100
        self.max_hp = self.hp + self.dop_hp
        self.recharge_healing = 0

        self.atk = 4 + (lv * 0.25) * 4
        self.dop_atk = 0
        self.atk_fire = 0
        self.status_atk = 0
        self.chance_of_miss = 0

        self.protect = 4 + (lv * 0.25) * 4
        self.dop_protect = 0
        self.status_protect = 0

        self.time_def = 0

        self.Consumable_items = ""
        self.recharge_Consumable_items = 0

        # ["Sword", "BodyArmor", "Gloves", "Greaves", "Helmet", "Ring"]
        self.items = ["default", "default", "default", "default", "default", "default", "default"]

    def update(self):
        self.anim.update(0)

    def attack(self, other):
        flag_miss = False
        if self.chance_of_miss != 0:
            chance = random.randint(0, 100)
            if chance <= self.chance_of_miss:
                flag_miss = True
        if not flag_miss:
            dm = items_Sword[self.items[0]].attack(self, other)
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
            if arr[i] != "":
                self.items[i] = arr[i]
        self.dop_protect = items_BodyArmor[self.items[1]].protect + items_Gloves[self.items[2]].protect + items_Greaves[
            self.items[3]].protect + items_Helmet[self.items[4]].protect
        self.status_protect = items_Helmet[self.items[4]].status_protect
        self.dop_atk = items_Gloves[self.items[2]].atk
        self.dop_hp += items_BodyArmor[self.items[1]].hp
        self.max_hp += self.dop_hp
        self.hp += self.dop_hp

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
    def __init__(self, filename, x, y, character, *group):
        super().__init__(*group)
        self.frames = []
        self.character = character
        for i in filename:
            i = pygame.image.load(i)
            i = pygame.transform.scale(i, (490, 400))
            self.frames.append(i)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, NewX):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.character == 'hero':
            self.rect.x = NewX
        else:
            self.rect.x = NewX + 450
