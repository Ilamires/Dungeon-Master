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
            dm = 0.2 * (self.atk + unit.atk + unit.dop_atk)
        dop_dm = (self.atk_fire + unit.atk_fire) * unit.atk_fire_multiplier - other.status_protect
        if dop_dm > 0:
            dm += dop_dm
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


class Ring:
    def __init__(self, atk_fire, poison_atk, poison_move):
        self.atk_fire = atk_fire
        self.poison_atk = poison_atk
        self.poison_move = poison_move


class Helmet:
    def __init__(self, protect, status_protect):
        self.protect = protect
        self.status_protect = status_protect


items_Sword = {"default": Sword(1, 0, 0),
               "rusty sword": Sword(5, 0, 0),
               "fire sword": Sword(5, 3, 5),
               "god sword": Sword(1000, 0, 0)}

items_BodyArmor = {"default": BodyArmor(1, 0),
                   "rusty body armor": BodyArmor(2, 20),
                   "fire body armor": BodyArmor(5, 50)}

items_Helmet = {"default": Helmet(0, 0),
                "rusty gloves": Helmet(1, 1),
                "fire gloves": Helmet(1, 3)}

items_Gloves = {"default": Gloves(0, 0),
                "rusty gloves": Gloves(2, 1),
                "fire gloves": Gloves(3, 1)}

items_Greaves = {"default": Greaves(0),
                 "rusty greaves": Greaves(1),
                 "fire greaves": Greaves(3)}

items_Ring = {"default": Ring(0, 0, 0),
              "rusty ring": Ring(5, 0, 0),
              "poison ring": Ring(0, 3, 2)}

Consumable_items = {"fireball": ["damage", 20, 3]}


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
