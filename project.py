#Dan Petruso
#CMPT 120L 113
from graphics import *

def initialize():
    global points
    points = 0

    global pointGain
    pointGain = 5

    global gameFinished
    gameFinished = False

    global locCount
    locCount = 0

    global numOfMoves
    numOfMoves = 0

    global playerName
    global rivalName

    location = [ "\nYou are now in your bedroom. You're bed is unmade and you're too lazy to make it. You see something on your desk."
                 "\nTo your east is the door to your living room. "
                 ,#0
                 "\nYou are now in your living room. Your mother is watching television and you're father is nowhere in site."
                 "\nTo the south is the front door. \nTo the west is the door to your bedroom. "
                 ,#1
                 "\nYou are now outside of your house. You notice a few pidgeys on your front lawn."
                 "\nTo your east is the tall grass. \nTo your north is your house. "
                 ,#2
                 "\nYou are now in the tall grass. It is too dangerous to stay here so you will need a Pokemon "
                 "from Professor Oak to protect yourself."
                 "\nTo the south is Oak's lab. \nTo the west is outside your house. "
                 ,#3
                 "\nYou are now in Oak's lab. He tells you to take the pokeball from the research room to the west."
                 "\nTo the west is the research room. \nTo the north is the exit. "
                 ,#4
                 "\nYou are now in the research room and there are pokeballs everywhere."
                 "\nTo the south is the battle arena. \nTo the east is the lab. "
                 ,#5
                 "\nYou entered the battle arena and " + rivalName + " would like to battle."
                 "\nTo the west is the Pokemon Center. \nTo the north is the research room."
                 ,#6
                 "\nYou arrived at the Pokemon Center and Nurse Joy healed your Pokemon. "
                 "You have to pick up a package for the professor at the PokeMart."
                 "\nTo the north is PokeMart. \nTo the east is the research room. "
                 ,#7
                 "\nYou arrived at the PokeMart and have to pick up the package. Professor Oak wants you "
                 "to give it to him at " + rivalName + "'s house."
                 "\nTo the west is " + rivalName + "'s house. \nTo the south is the Pokemon Center. "
                 ,#8
                 "\nYou arrived at " + rivalName + "'s house and Professor Oak would like the package you were supposed to pick up."
                 #9
                 ]

    shortLocation = [ "\nYou are now in your bedroom. East is the door to your living room. "
                      ,#0
                      "\nYou are now in your living room. South is the front door. West is your bedroom. "
                      ,#1
                      "\nYour are now outside your house. East is the tall grass. North is your house. "
                      ,#2
                      "\nYou are now in the tall grass. South is Oak's lab. West is outside your house. "
                      ,#3
                      "\nYou are now in Oak's Lab. West is research room. North is the exit. "
                      ,#4
                      "\nYou are now in the research room. South is the battle arena. East is the lab. "
                      ,#5
                      "\nYou are now in the battle arena. West is Pokemon Center. North is research room. "
                      ,#6
                      "\nYou are now in the Pokemon Center. North is PokeMart. East is research room. "
                      ,#7
                      "\nYou are now in the PokeMart. West is " + rivalName + "'s house. South is Pokemon Center. "
                      ,#8
                      "\nYou are at " + rivalName + "'s house. East is PokeMart. "
                      ,#9
                      ]
    
    
    global searchLocation
    searchLocation = ["There is a map on your desk. "
                      ,#0
                      "There is no item here. "
                      ,#1
                      "There is no item here. "
                      ,#2
                      "There is no item here. "
                      ,#3
                      "There is no item here. "
                      ,#4
                      "There is a pokeball on the table that you can take. "
                      ,#5
                      "There is no item here. "
                      ,#6
                      "There is no item here. "
                      ,#7
                      "There is a package you need to pick up. "
                      ,#8
                      "There is no item here. "
                      ,#9
                      ]
    


    global gameWon
    gameWon = False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def intro():
    print("Choose Your Pokemon!")
    print("This is a game where you will choose your first Pokemon and start your first battle.")
    print("Every new move you will gain 5 points.")

def customize():
    global playerName
    global rivalName
    playerName = input("Professor Oak: 'Welcome to the world of Pokemon, what is your name?' ")

    rivalName = input("Professor Oak: 'Hello " + playerName + ", this is my grandson and your rival, what was his name again?' ")
    
    print("Professor Oak: 'Oh yes, it was " + rivalName + ". Great! Now you have begun your journey!'\n ")

    print("-------------------------------------------------------------------\n")

def ending():
    global gameWon
    if gameWon == True:
        print("Congrats! You won the game!")
    elif gameWon == False:
        print("Game Over! You didn't complete all the requirements.")
    getCopyright()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getCopyright():
    print("Copyright (c) 2107 Daniel Petruso, daniel.petruso1@marist.edu")



def directionToNum(direction):
    change = {
        "north" : 0,
        "south" : 1,
        "east"  : 2,
        "west"  : 3}
    return change[direction]

    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game():
   
    mapMatrix = [   #  North       South       East        West
                    [  None,       None,       1,          None     ]    #Bedroom       0
                ,   [  None,       2,          None,       0        ]    #Livingroom    1
                ,   [  1,          None,       3,          None     ]    #Outside       2
                ,   [  None,       4,          None,       2        ]    #Tall Grass    3
                ,   [  3,          None,       None,       5        ]    #Oaks Lab      4
                ,   [  None,       6,          4,          None     ]    #Research Room 5
                ,   [  5,          None,       None,       7        ]    #Battle Arena  6
                ,   [  8,          None,       6,          None     ]    #Pkmn Center   7
                ,   [  None,       7,          None,       9        ]    #PokeMart      8
                ,   [  None,       None,       8,          None     ]    #Rivals House  9
                ]

    global playerName
    global rivalName
    global gameFinished
    global locCount
    
    print(locationLength(locCount))
    
    while gameFinished == False:

        if locCount == 9 and canUse[2] == False: #player loses game if they go to last location without item.
            gameFinished = True
            gameWon = False
            break

        choice = input()
        choice = choice.lower()
        choice = choice.strip()
        
        if choice == "north" or choice == "south" or choice == "east" or choice == "west":
            num = directionToNum(choice)
            move = mapMatrix[locCount][num]
            goto(move)

        else:
            messageSorter(choice)

                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    
    win = GraphWin("window",400,300)
    win.setCoords(0,0,10,10)
    output = Text(Point(5,6), "XXXXXXXXXXX")
    output.draw(win)

    intro()
    customize()
    initialize()
    game()
    ending()
    
main()
