import pygame
import random
from items import Consumable_items, items_Sword, items_BodyArmor, items_Gloves, items_Greaves, items_Ring, items_Helmet, \
    items_Artefacts


class Unit:
    def __init__(self, lv, filename, x, y, character, *group):
        self.anim = AnimatedSprite(filename, x, y, character, *group)
        self.image = self.anim.image
        self.flag_first_move = True

        self.dop_hp = 0
        self.hp = 100 + (lv * 0.25) * 100
        self.max_hp = self.hp + self.dop_hp
        self.healing_hp = 50
        self.recharge_healing = 0
        self.max_recharge_healing = 6

        self.atk = 4 + (lv * 0.25) * 4
        self.dop_atk = 0

        self.atk_fire = 0
        self.atk_fire_multiplier = 1

        self.status_atk = 0
        self.chance_of_miss = 0

        self.protect = 4 + (lv * 0.25) * 4
        self.dop_protect = 0
        self.status_protect = 0
        self.poison_dm = 0
        self.poison_move = 0
        self.poison_flag = False

        self.time_def = 0

        self.Consumable_items = ""
        self.recharge_Consumable_items = 0
        self.revival = 0

        # ["Sword", "BodyArmor", "Gloves", "Greaves", "Helmet", "Ring"]
        self.items = ["default", "default", "default", "default", "default", "default"]
        self.artefacts = []
        self.active_artefacts = []
        for i in self.artefacts:
            items_Artefacts[i][0].use(self)
            if items_Artefacts[i][1] == 1:
                self.active_artefacts.append(i)

    def update(self):
        self.anim.update(0)

    def attack(self, other):
        if self.flag_first_move:
            for i in self.active_artefacts:
                items_Artefacts[i][0].active_use(other)
            self.flag_first_move = False
        flag_miss = False
        if self.poison_flag:
            other.poison_move = items_Ring[self.items[5]].poison_move
            other.poison_dm = items_Ring[self.items[5]].poison_atk
        if self.chance_of_miss != 0:
            chance = random.randint(0, 100)
            if chance <= self.chance_of_miss:
                flag_miss = True
        if not flag_miss:
            dm = items_Sword[self.items[0]].attack(self, other)
        else:
            dm = 0
        return dm

    def use_consumable_items(self):
        if self.recharge_Consumable_items == 0:
            name = self.Consumable_items
            type = Consumable_items[name][0]
            type_atk = Consumable_items[name][1]
            if type == "damage":
                if type_atk == "fire":
                    dm = Consumable_items[name][2] * self.atk_fire_multiplier
                    self.recharge_Consumable_items = Consumable_items[name][3]
                    return round(dm)

    def get_info_consumable_item(self):
        name = self.Consumable_items
        type = Consumable_items[name][0]
        type_atk = Consumable_items[name][1]
        if type == "damage":
            arr = [name, type, type_atk]
            return arr

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
        if items_Ring[self.items[5]].poison_move > 0:
            self.poison_flag = True

    def putting_artefacts(self, arr):
        for i in arr:
            if i != "":
                items_Artefacts[i][0].use(self)
                if items_Artefacts[i][1] == 1:
                    self.active_artefacts.append(i)
                self.artefacts.append(i)

    def putting_on_consumable_items(self, name):
        self.Consumable_items = name

    def taking_damage(self, dm):
        self.hp -= dm
        if self.hp < 0:
            self.hp = 0
            if self.revival > 0:
                self.hp = self.max_hp * 0.5
                self.revival -= 1

    def defense(self):
        self.time_def = items_BodyArmor[self.items[1]].defense(self)

    def healing(self):
        if self.recharge_healing == 0:
            self.heal(self.healing_hp)
            self.recharge_healing = self.max_recharge_healing

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
        if self.poison_move > 0:
            self.taking_damage(self.poison_dm)
            self.poison_move -= 1
            if self.poison_move == 0:
                self.poison_dm = 0


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, character, *group):
        super().__init__(*group)
        self.fps = 0
        self.frames = []
        self.character = character
        for i in filename:
            i = pygame.image.load(i)
            # i = pygame.transform.scale(i, (360, 400))
            self.frames.append(i)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, NewX):
        if self.fps % 6 == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            if self.character == 'hero':
                self.rect.x = NewX
            else:
                self.rect.x = NewX + 490
        self.fps += 1
