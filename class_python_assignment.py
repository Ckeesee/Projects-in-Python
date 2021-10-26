DefaultClasses = [Bard, Paladin, Fighter, Rogue, Wizard, Cleric, Warlock]
DefaultWeapons = [Sword, Shield]
class Player:
    name = 'No Name Provided'
    characterName = ''

class PickClass(Player):
    print("Pick  a class!\n")
    for x in DefaultClasses:
        print(x)
    pickClass = input("Enter Class:")
    for x in DefaultClasses:
        if pickClass in DefaultClasses:
            characterClass = x
        else:
            pickClass = input("Please pick a Class from the list:")
    if characterClass = Fighter or Rogue:
        spells = 0
    else:
        spells = 3

class PickEquip(Player):
    characterWeapon = input("Please input your weapon of choice for your character:")
    characterArmor = input("Please input your armor of choice for your character:")
    print("You chose " + characterWeapon + " and " + characterArmor + " as your equipment of choice!")
    
