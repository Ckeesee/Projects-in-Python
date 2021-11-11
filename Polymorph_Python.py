#Creats a parent class of organisum and prints out the information
class Organisum:
    species="unknown"
    habitat="unknown"
    legs=0
    arms=0
    def information(self):
        msg = "Species: {}\nHabitat: {}\nNumber of Legs: {}\nNumber of arms: {}\n".format(self.species,self.habitat,self.legs,self.arms)
        return msg
#Create the child class using the parent class of organisum to make a human  and print out their feats
class Human(Organisum):
    species="Human"
    habitat = "Land"
    legs =2
    arms= 2
    gender="non-bianary"
    haircolor="Blonde"
    

    def feats(self):
        msg= "\nHumans have amazing feats that they can accomplish if they put their minds to it!"
        return msg
    def information(self):
        msg = "Species: {}\nHabitat: {}\nNumber of Legs: {}\nNumber of arms: {}\nGender: {}\nHair Color: {}\n".format(self.species,self.habitat,self.legs,self.arms,self.gender,self.haircolor)
        return msg

#Creats a second child class making a sloth and explaining their typical movement patterns
class Sloth(Organisum):
    species="Sloth"
    habitat="Jungle and Rainforests"
    legs=2
    arms=2
    furColor="Grey"
    food="Insects"

    def movement(self):
        msg = "\nSloths spend most of their lives upsidown and if they flip right side up it is hard for them to move efficently"
        return msg
    def information(self):
        msg = "Species: {}\nHabitat: {}\nNumber of Legs: {}\nNumber of arms: {}\nFur Color: {}\nTypical Food: {}\n".format(self.species,self.habitat,self.legs,self.arms,self.furColor,self.food)
        return msg



if __name__== "__main__":
    human = Human()
    print(human.information())
    print(human.feats())

    sloth=Sloth()
    print(sloth.information())
    print(sloth.movement())
   
