class Sword:
    def __init__(self, atk, atk_fire, vampirism):
        self.atk = atk
        self.atk_fire = atk_fire
        self.vampirism = vampirism

    def attack(self, unit, other):
        if other.time_def == 0:
            dm = (self.atk + unit.atk) - (other.protect + other.dop_protect)
        else:
            dm = (self.atk + unit.atk) - other.time_def
        other.time_def = 0
        if dm < 0.2 * (self.atk + unit.atk):
            dm = 0.2 * (self.atk + unit.atk) + self.atk_fire
        else:
            dm += self.atk_fire
        if self.vampirism != 0:
            unit.heal(round((self.vampirism / 100) * dm))
        return dm


class BodyArmor:
    def __init__(self, protect):
        self.protect = protect

    def defense(self, unit):
        return (self.protect + unit.protect) * 2


items_sword = {"default": Sword(1, 0, 0),
               "rusty sword": Sword(5, 0, 0),
               "fire sword": Sword(5, 3, 5)}

items_BodyArmor = {"default": BodyArmor(1),
                   "rusty body armor": BodyArmor(5),
                   "fire body armor": BodyArmor(10)}

Consumable_items = {"fireball": ["damage", 20, 3]}
