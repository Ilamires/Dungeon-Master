class Sword:
    def __init__(self, name, atk, atk_fire, vampirism):
        self.name = name
        self.atk = atk
        self.atk_fire = atk_fire
        self.life_steal = vampirism

    def attack(self, unit, other, flag):
        if other.time_def == 0:
            dm = (self.atk + unit.atk + unit.dop_atk) - (other.protect + other.dop_protect) * other.protect_multiplier
        else:
            dm = (self.atk + unit.atk + unit.dop_atk) - other.time_def
        other.time_def = 0
        if dm < 0.2 * (self.atk + unit.atk + unit.dop_atk):
            dm = 0.2 * (self.atk + unit.atk + unit.dop_atk)
        dop_dm = (self.atk_fire + unit.atk_fire) * unit.atk_fire_multiplier - other.status_protect
        if dop_dm > 0:
            dm += dop_dm
        if self.life_steal != 0 and flag:
            unit.heal(round((self.life_steal / 100) * dm))
        return round(dm)

    def get_stats(self):
        arr_str = [f"name = {self.name}", f"attack = {self.atk}", f"attack fire = {self.atk_fire}",
                   f"life_steal = {self.life_steal}"]
        return arr_str


class BodyArmor:
    def __init__(self, name, protect, hp):
        self.name = name
        self.hp = hp
        self.protect = protect

    def defense(self, unit):
        return (self.protect + unit.protect) * 2 * unit.protect_multiplier

    def get_stats(self):
        arr_str = [f"name = {self.name}", f"hp = {self.hp}", f"protect = {self.protect}"]
        return arr_str


class Gloves:
    def __init__(self, name, atk, protect):
        self.name = name
        self.atk = atk
        self.protect = protect

    def get_stats(self):
        arr_str = [f"name = {self.name}", f"atk = {self.atk}", f"protect = {self.protect}"]
        return arr_str


class Greaves:
    def __init__(self, name, protect):
        self.name = name
        self.protect = protect

    def get_stats(self):
        arr_str = [f"name = {self.name}", f"protect = {self.protect}"]
        return arr_str


class Ring:
    def __init__(self, name, atk_fire, poison_atk, poison_move):
        self.name = name
        self.atk_fire = atk_fire
        self.poison_atk = poison_atk
        self.poison_move = poison_move

    def get_stats(self):
        arr_str = [f"name = {self.name}", f"atk fire = {self.atk_fire}", f"poison atk = {self.poison_atk}",
                   f"poison move = {self.poison_move}"]
        return arr_str


class Helmet:
    def __init__(self, name, protect, status_protect):
        self.name = name
        self.protect = protect
        self.status_protect = status_protect

    def get_stats(self):
        arr_str = [f"name = {self.name}", f"protect = {self.protect}", f"status_protect = {self.status_protect}"]
        return arr_str


# ["Sword", "BodyArmor", "Gloves", "Greaves", "Helmet", "Ring"]
items_Sword = {"default": Sword("default", 1, 0, 0),
               "rusty sword": Sword("rusty sword", 5, 0, 0),
               "fire sword": Sword("fire sword", 5, 3, 5),
               "Dima sword": Sword("Dima sword", 1000, 1000, 1000)}

items_BodyArmor = {"default": BodyArmor("default", 1, 0),
                   "rusty body armor": BodyArmor("rusty body armor", 2, 20),
                   "fire body armor": BodyArmor("fire body armor", 5, 50)}

items_Gloves = {"default": Gloves("default", 0, 0),
                "rusty gloves": Gloves("rusty gloves", 2, 1),
                "fire gloves": Gloves("fire gloves", 3, 1)}

items_Greaves = {"default": Greaves("default", 0),
                 "rusty greaves": Greaves("rusty greaves", 1),
                 "fire greaves": Greaves("fire greaves", 3)}

items_Helmet = {"default": Helmet("default", 0, 0),
                "rusty gloves": Helmet("rusty gloves", 1, 1),
                "fire gloves": Helmet("fire gloves", 1, 3)}

items_Ring = {"default": Ring("default", 0, 0, 0),
              "rusty ring": Ring("rusty ring", 5, 0, 0),
              "poison ring": Ring("poison ring", 0, 3, 2)}

Consumable_items = {"fireball": ["damage", "fire", 20, 4]}


class Artefacts:
    def __init__(self):
        pass

    def use(self, hero):
        pass


class Dio(Artefacts):
    def use(self, hero):
        hero.revival += 1


class OilBottle(Artefacts):
    def use(self, hero):
        hero.atk_fire_multiplier += 0.25

    def active_use(self, enemy):
        enemy.chance_of_miss += 10


class Lantern(Artefacts):
    def use(self, hero):
        if hero.chance_of_miss > 0:
            hero.chance_of_miss -= 5
            if hero.chance_of_miss < 0:
                hero.chance_of_miss = 0

    def active_use(self, enemy):
        enemy.chance_of_miss += 5


class Torch(Artefacts):
    def use(self, hero):
        if hero.chance_of_miss > 0:
            hero.chance_of_miss -= 3
            if hero.chance_of_miss < 0:
                hero.chance_of_miss = 0
        hero.atk_fire += 7


class MegaShield(Artefacts):
    def use(self, hero):
        hero.protect_multiplier += 0.5


items_Artefacts = {"Dio": [Dio(), 0],
                   "Oil Bottle": [OilBottle(), 1]}

#  название : [1)Максимум хп, 2)восстановление здововья, 3)атака, 4)атака(множитель), 5)атака огнем,
#  6)атака ядом, 7)вампиризм, 8)дополнительная защита, 9)шанс промаха%, 10)шанс промаха%(дебафф на врага),
#  11)эффект масла(значение влияет только на шанс промаха, увееличение урона от огня фиксированное)]
items_artefacts = {
    "Ash": [0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0],
    "Lantern": [0, 0, 0, 0, 0, 0, 0, -5, 5, 0],
    "MegaShield": [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0],
    "Heart": [100, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Vampire Tooth": [0, 0, 7, 0, 0, 0, 15, 0, 0, 0, 0],
    "Poison bottle": [0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0],
    "Oil bottle": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
    "Blessing": [50, 2, 5, 0, 0, 0, 0, 3, -3, 0, 0],
    "Torch": [0, 0, 0, 0, 7, 0, 0, 0, -3, 0, 0],
    "Ice cage": [0, 0, 0, 0, 0, 0, 0, 15, 10, 0, 0]
}
