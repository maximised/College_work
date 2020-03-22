class Human:
    def __init__(self, name, skill, own_weapon):
        self.__name = name
        if skill < 0:
            raise ValueError("skill can't be lower than 0")
        self.__skill = skill
        self.__own_weapon = bool(own_weapon)

    def __str__(self):
        return "Human (name = {}, skill = {}, Have weapon = {})".format(self.__name, self.__skill,
                                                                                    bool(self.__own_weapon))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, skill):
        self.__skill = skill
        if self.__skill < 0:
            raise ValueError("skill can't be lower than 0")

    def getOwn_weapon(self):
        return self.__own_weapon

    def setOwn_weapon(self, own_weapon):
        self.__own_weapon = own_weapon

    # name = property(getName, setName)
    # skill = property(getSkill, setSkill)

    own_weapon = property(getOwn_weapon, setOwn_weapon)

    def __gt__(self, o):
        if self.own_weapon == True and o.own_weapon == True:
            return self.skill > o.skill
        if self.own_weapon == False and o.own_weapon == False:
            return self.strength > o.strength
        return self.own_weapon > o.own_weapon

    def attack(self, other):
        if (isinstance(self, Archer) or isinstance(self, Knight)) and (isinstance(other, Archer) or isinstance(other, Knight)):
            raise ValueError("Knights and Archers can't fight against each other")
        if (self.__class__ != Orc and not self.own_weapon) or (other.__class__ != Orc and not other.own_weapon):
            raise ValueError("Archers and Knights can't fight without weapons!")

        if self > other:
            self.skill *= 1.05
            print(self.name + ' is vicorious!')
        elif other > self:
            other.skill *= 1.05
            print(other.name + ' is vicorious!')
        else:
            print('Nobody is victorious.')

class Orc(Human):
    def __init__(self, name, skill, own_weapon, strength):
        Human.__init__(self, name, skill, own_weapon)
        if strength < 0:
            raise ValueError("strength can't be lower than 0")
        self.__strength = strength

    def __str__(self):
        return "Orc (name = {}, skill = {}, strength = {}, Have weapon = {})".format(self.name, self.skill,
                                                                                       self.strength,
                                                                                    bool(self.own_weapon))

    def getStrength(self):
        return self.__strength

    def setStrength(self, strength):
        self.__strength = strength
        if self.__strength < 0:
            raise ValueError("strength can't be lower than 0")

    strength = property(getStrength, setStrength)

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


class Knight(Human):
    def __init__(self, name, skill, own_weapon, kingdom, archers):
        Human.__init__(self, name, skill, own_weapon)
        self.__kingdom = kingdom
        if any(not isinstance(a, Archer) for a in archers):
            raise ValueError("The knight can only lead archers")
        self.__archers = list(archers)

    def __str__(self):
        return("Knight (name: {}, skill: {}, own_weapon: {}, kingdom: {}, "
               "archers lead: {}".format(self.name, self.skill, self.own_weapon, self.kingdom,
                                         ', '.join([a.name for a in self.archers])))

    def getArchers(self):
        return self.__archers

    def setArchers(self, archers):
        self.__archers = archers

    def getKingdom(self):
        return self.__kingdom

    def setKingdom(self, kingdom):
        self.__kingdom = kingdom

    kingdom = property(getKingdom, setKingdom)
    archers = property(getArchers, setArchers)