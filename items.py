class Sword:
    def __init__(self, atk, atk_fire, vampirism):
        self.atk = atk
        self.atk_fire = atk_fire
        self.vampirism = vampirism

    def attack(self, unit, other):
        if other.time_def == 0:
            dm = (self.atk + unit.atk + unit.dop_atk) - (other.protect + other.dop_protect)
        else:
            dm = (self.atk + unit.atk + unit.dop_atk) - other.time_def
        other.time_def = 0
        if dm < 0.2 * (self.atk + unit.atk + unit.dop_atk):
            dm = 0.2 * (self.atk + unit.atk + unit.dop_atk) + self.atk_fire
        else:
            dm += self.atk_fire
        if self.vampirism != 0:
            unit.heal(round((self.vampirism / 100) * dm))
        return round(dm)


class BodyArmor:
    def __init__(self, protect, hp):
        self.hp = hp
        self.protect = protect

    def defense(self, unit):
        return (self.protect + unit.protect) * 2


class Gloves:
    def __init__(self, atk, protect):
        self.atk = atk
        self.protect = protect


class Greaves:
    def __init__(self, protect):
        self.protect = protect


items_Sword = {"default": Sword(1, 0, 0),
               "rusty sword": Sword(5, 0, 0),
               "fire sword": Sword(5, 3, 5)}

items_BodyArmor = {"default": BodyArmor(1, 0),
                   "rusty body armor": BodyArmor(2, 20),
                   "fire body armor": BodyArmor(5, 50)}

items_Gloves = {"default": Gloves(0, 0),
                "rusty gloves": Gloves(2, 1),
                "fire gloves": Gloves(3, 1)}

items_Greaves = {"default": Greaves(0),
                 "rusty greaves": Greaves(1),
                 "fire greaves": Greaves(3)}

Consumable_items = {"fireball": ["damage", 20, 3]}
