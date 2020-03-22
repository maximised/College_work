from archer import Archer

class Knight(Archer):
    def __init__(self, name, skill, own_weapon, kingdom):
        Archer.__init__(self, name, skill, own_weapon, kingdom)
        self.archers = []