from human import Human, Orc, Archer, Knight


orc1 = Orc('larry', 12, True, 10)
orc2 = Orc('jim', 10, False, 12)
print(orc1)
print(orc2)
print(isinstance(orc1, Archer))

orc1.attack(orc2)

print(orc1)
print(orc2)

arc1 = Archer('hans', 13, True, 'cork')
print(arc1)

orc1.attack(arc1)
print(arc1)

arc2 = Archer('sans', 10, True, 'cork')

knight = Knight('gon', 15, True, 'Dublin', [])
print(knight)

knight.attack(orc1)

print(knight)

orc1.attack(orc1)

print(orc1)






#################################################
import shelve

orc_shelf = Orc('Kong', 20, True, 20)
archer_shelf = Archer('Shawn', 15, True, 'Gondor')
knight_shelf = Knight('Clide', 10, True, 'Saradin', [archer_shelf, arc1])

def shelf(char):
    if isinstance(char, Orc):
        t = 'orc'
    elif isinstance(char, Archer):
        t = 'archers'
    elif isinstance(char, Knight):
        t = 'knight'
    else:
        print("Incompatible object")
        return

    db = shelve.open(t)
    db[char.name] = char

    print(db[char.name])

    db.close()

shelf(orc_shelf)
shelf(archer_shelf)
shelf(knight_shelf)