class Sword:
    def __init__(self, atk, atk_fire, vampirism):
        self.atk = atk
        self.atk_fire = atk_fire
        self.vampirism = vampirism

    def attack(self, hero, other):
        if other.time_def == 0:
            dm = (self.atk + hero.atk) - (other.protect + other.dop_protect)
        else:
            dm = (self.atk + hero.atk) - other.time_def
        other.time_def = 0
        if dm < 0.2 * (self.atk + hero.atk):
            dm = 0.2 * (self.atk + hero.atk) + self.atk_fire
        else:
            dm += self.atk_fire
        if self.vampirism != 0:
            hero.heal(round((self.vampirism / 100) * dm))
        return dm


items_sword = {"default": Sword(1, 0, 0),
               "rusty sword": Sword(5, 0, 0),
               "fire sword": Sword(5, 3, 5)}

Consumable_items = {"fireball": ["damage", 20, 3]}
