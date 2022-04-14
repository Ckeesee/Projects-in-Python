#Initalizing the base classes for D&D
DefaultClasses = ["Bard", "Paladin", "Fighter", "Rogue", "Wizard", "Cleric", "Warlock"]
#Creatiing a player for Dungeons and Dragons
#Making a player and character name
class Player:
    name = 'No Name Provided'
    characterName = ''


#Picking the Player's Character's class from a list and seeing if they get spells
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
    if characterClass == "Fighter" or characterClass == "Rogue":
        spells = 0
    else:
        spells = 3

#Player gets to choose what equipment that their character gets to use
class PickEquip(Player):
    characterWeapon = input("Please input your weapon of choice for your character:")
    characterArmor = input("Please input your armor of choice for your character:")
    print("You chose " + characterWeapon + " and " + characterArmor + " as your equipment of choice!")
    
