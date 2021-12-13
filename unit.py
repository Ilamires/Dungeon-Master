class Unit:

    def __init__(self, lv):
        self.hp = 100 + (lv * 0.25) * 100
        self.atk = 10 + (lv * 0.25) * 10
        self.protect = 4 + (lv * 0.25) * 4
        self.dop_atk = 0
        self.dop_protect = 0

    def attack(self, other):
        dm = (self.atk + self.dop_atk) - (other.protect + other.dop_protect)
        if dm < 0.2 * (self.atk + self.dop_atk):
            return 0.2 * (self.atk + self.dop_atk)
        else:
            return dm

    def taking_damage(self, dm):
        self.hp -= dm

    def defense(self):
        return (self.protect + self.dop_protect) * 2
