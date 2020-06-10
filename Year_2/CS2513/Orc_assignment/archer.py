from human import Human

class Archer(Human):
    def __init__(self, name, skill, own_weapon, kingdom):
        Human.__init__(self, name, skill, own_weapon)
        self.__kingdom = kingdom

    def __str__(self):
        return "Archer (name = {}, skill = {}, Have weapon = {}, kingdom = {})".format(self.name, self.skill,
                                                                        bool(self.own_weapon), self.kingdom)

    def getKingdom(self):
        return self.__kingdom

    def setKingdom(self, kingdom):
        self.__kingdom = kingdom

    kingdom = property(getKingdom, setKingdom)

