class Orc:
    def __init__(self, name, skill, strength, own_weapon):
        self.__name = name
        if skill < 0:
            raise ValueError("skill can't be lower than 0")
        self.__skill = skill
        if strength < 0:
            raise ValueError("strength can't be lower than 0")
        self.__strength = strength
        self.__own_weapon = bool(own_weapon)

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

    def getStrength(self):
        return self.__strength

    def setStrength(self, strength):
        self.__strength = strength
        if self.__strength < 0:
            raise ValueError("strength can't be lower than 0")

    def getOwn_weapon(self):
        return self.__own_weapon

    def setOwn_weapon(self, own_weapon):
        self.__own_weapon = own_weapon

    # name = property(getName, setName)
    # skill = property(getSkill, setSkill)
    strength = property(getStrength, setStrength)
    own_weapon = property(getOwn_weapon, setOwn_weapon)

    def __str__(self):
        return "Orc (name = {}, skill = {}, strength = {}, Have weapon = {}".format(self.__name, self.__skill,
                                                                                    self.__strength,
                                                                                    bool(self.__own_weapon))

    def __gt__(self, o):
        if self.__own_weapon == True and o.own_weapon == True:
            return self.__skill > o.skill
        if self.__own_weapon == False and o.own_weapon == False:
            return self.__strength > o.strength
        return self.__own_weapon > o.own_weapon

    def attack(self, other):
        if self > other:
            self.__skill *= 1.05
            print(self.__name + ' is vicorious!')
        elif other > self:
            other.skill *= 1.05
            print(other.name + ' is vicorious!')
        else:
            print('No orc is victorious.')

