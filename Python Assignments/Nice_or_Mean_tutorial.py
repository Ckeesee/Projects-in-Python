import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

import colorama
from colorama import init, Fore, Back, Style
init()




def start(nice=0,mean=0,name=""):
    #get user name
    name=describe_game(name)
    nice,mean,name= nice_mean (nice,mean,name)



def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the users name,
        If not a new game, thank the player for playing
        again and continue with the game
    """
    #meaning, if we do not already have this user name,
    #then they are a new player and we need to get their name
    if name!="":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name !="":
                    print("Welcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop=False
    return name


def nice_mean(nice,mean,name):
    stop=True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice\nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            color.write(" \nThe stranger walks away smiling...","STRING")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            color.write("\nThe stranger glares at you \nmenacingly and storms off...","COMMENT")
            mean = (mean +1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice >2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    #sub the {} widlcards with our variable values
    print("\nNice job{}, you win! \nEveryone loves you and you've \nmade lost of friends along the way!".format(name))
    #call again function and passin our variabels
    again(nice,mean,name)


def lose(nice,mean,name):
    #sub the {} wildards with our variable valuse
    print("\nAhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call play again function
    again(nice,mean,name)




def again(nice,mean,name):
    stop=True
    while stop:
        choice = input("\nDo you want to play again? (y/n):/n>>> ").lower()
        if choice =="y":
            stop=False
            reset(nice,mean,name)
        if choice =="n":
            print("\nOh, so sad, sorry to see you go!")
            stop=False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice i do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)
            












if __name__=="__main__":
    start()
        
