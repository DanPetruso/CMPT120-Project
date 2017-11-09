#Dan Petruso
#CMPT 120L 113
points = 0
visitedLocation = [False, False, False, False, False, False, False, False, False, False]
pointGain = 5
gameFinished = False
locCount = 0
numOfMoves = 0
playerName = ""
rivalName = ""

location = [ "\nYou are now in your bedroom. You're bed is unmade and you're too lazy to make it. You see something on your desk. \nTo your east is the door to your living room. "
             ,#0
             "\nYou are now in your living room. Your mother is watching television and you're father is nowhere in site."
             "\nTo the south is the front door. \nTo the west is the door to your bedroom. "
             ,#1
             "\nYou are now outside of your house. From the you notice a few pidgeys on your front lawn. \nTo your east is the tall grass. \nTo your north is your house. "
             ,#2
             "\nYou are now in the tall grass. It is too dangerous to stay here so you will need a Pokemon from Professor Oak to protect yourself."
             "\nTo the south is Oak's lab. \nTo the west is outside your house. "
             ,#3
             "\nYou are now in Oak's lab. He tells you to take the pokeball from the research room to the west."
             "\nTo the west is the research room. \nTo the north is the exit. "
             ,#4
             "\nYou are now in the research room and there is a pokeball on the table."
             "\nTo the south is the battle arena. \nTo the east is the lab. "
             ,#5
             "\nYou entered the battle arena and " + rivalName + " would like to battle."
             "\nTo the west is the Pokemon Center. \nTo the north is the research room."
             ,#6
             "\nYou arrived at the Pokemon Center and Nurse Joy healed your Charmander. You have to pick up a package for the professor at the PokeMart."
             "\nTo the north is PokeMart. \nTo the east is the research room. "
             ,#7
             "\nYou arrived at the PokeMart and have to pick up the package. Professor Oak wants you to give it to him at " + rivalName + "'s house."
             "\nTo the west is " + rivalName + "'s house. \nTo the south is the Pokemon Center. "
             ,#8
             "\nYou arrived at " + rivalName + "'s house and delivered the package. Thanks for playing! "
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
                  "There is a pokeball on the table. "
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

inventory = ["map", "pokeball", "package"]
canUse = [False, False, False]
itemUsed = ["You received the map!"
            ,#0
            "You threw the pokeball and out came Charmander. You began your first battle against " + rivalName + "'s Squirtle."
            "/nSquirtle used tackle! Charmander used Scratch! Charmander won the battle! Charmander is now tired and would like to rest up at the Pokemon Center."
            ,#1
            "You delivered the package to Professor Oak. In return, he rewards you with a Pokedex."
            #2
            ]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def intro():
    global playerName
    global rivalName
    print("Choose Your Pokemon!")
    print("This is a game where you will choose your first Pokemon and start your first battle.")
    print("Every new move you will gain", pointGain, "points.")

    playerName = input("Professor Oak: 'Welcome to the world of Pokemon, what is your name?' ")

    rivalName = input("Professor Oak: 'Hello " + playerName + ", this is my grandson and your rival, what was his name again?' ")
    
    print("Professor Oak: 'Oh yes, it was " + rivalName + ". Great! Now you have begun your journey!'\n ")

    print("-------------------------------------------------------------------\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getCopyright():
    print("Copyright (c) 2107 Daniel Petruso, daniel.petruso1@marist.edu")

def getHelp():
    print("\nValid commands for the game are North, South, East, West. \nNot all commands will work for all locations."
          "\nType Help to review the commands and Quit to exit game.\n")

def getErrorMessage():
    print("\nError. Invalid command.\n")

def getWrongWay():
    print("\nYou cannot move at that direction in this location.")

def getLongLocation():
    global location
    global locCount
    print(location[locCount])

def messageSorter(choice):
    global gameFinished

    if choice == "help":
        getHelp()

    elif choice == "quit":
        gameFinished = True
        print("You just quit the game.")
        locCount = -1 #breaks out of initial loop

    elif choice == "points":
        getPoints()

    elif choice == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
        getWrongWay()

    elif choice == "map":
        getMap()

    elif choice == "look":
        getLongLocation()

    else:
        getErrorMessage()


def getMap():
    print("\nMap:\n"
          "                           Bedroom ----- Living Room                    \n"
          "                                               |                        \n"
          "                                               |                        \n"
          "                                   Outside of House ----- Tall Grass    \n"
          "                                                                 |      \n"
          "                                                                 |      \n"
          "   Rivals House ----- PokeMart           Research Room  ----- Oaks Lab  \n"
          "                        |		        |                          \n"
          "                        |  		        |                          \n"
          "                  Pokemon Center ----- Battle Arena                     \n\n")



def directionToNum(direction):
    change = {
        "north" : 0,
        "south" : 1,
        "east"  : 2,
        "west"  : 3}
    return change[direction]

    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pointChecker(count):
    global points
    global visitedLocation
    global pointGain
    global locCount

    if count == -1: #gives total amount of points to user
        print("\nTotal points: " + str(points))

    if visitedLocation[locCount] == False:
        points += pointGain
        visitedLocation[locCount] = True

def locationLength(count):
    global location
    global shortLocation
    global visitedLocation
    if visitedLocation[count] == False:
        return location[count]
    else:
        return shortLocation[count]

def getPoints():
    return pointChecker(-1)

def getLocation():
    global visitedLocation
    global location
    global shortLocation

def goto(counter):
    global locCount
    pointChecker(locCount)
    locCount = counter
    timer()

def timer():
    global numOfMoves
    global locCount
    global gameFinished
    numOfMoves+=1
    print("Total number of moves:", numOfMoves)
    if numOfMoves == 15:
        print("You have been out for a long time and your mother wants you home. Game Over.")
        gameFinished = True
        locCount = -1
        
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
    
    while gameFinished == False:

        choice = input(locationLength(locCount))
        choice = choice.lower()
        choice = choice.strip()
        
        if choice == "north" or choice == "south" or choice == "east" or choice == "west":
            num = directionToNum(choice)
            move = mapMatrix[locCount][num]
            goto(move)
            
        else:
            messageSorter(choice)

        
    while False:
        #Location0: Bedroom
        while locCount == 0:
            choice = input(location[0])
            
            if choice.lower() == "east":
                print("You proceeded into the living room where your mother is watching television.\n\n")
                goto(1)
                
            else:
                messageSorter(choice)

        #Location1: Living Room
        while locCount == 1:
            choice = input(location[1])
            
            if choice.lower() == "west":
                print("You proceeded back into your room.\n\n")
                goto(0)

            elif choice.lower() == "south":
                print("You headed out the door. \nMom:'Goodbye", playerName + ", have a nice day!\n\n")
                goto(2)
                
            else:
                messageSorter(choice)

        #Location2: Outside
        while locCount == 2:
            choice = input(location[2])
            
            if choice.lower() == "north":
                print("You proceeded back into your house.\n\n")
                goto(1)

            elif choice.lower() == "east":
                print("You headed towards the tall grass.\n\n")
                goto(3)
                
            else:
                messageSorter(choice)

        #Location3: Tall Grass
        while locCount == 3:
            choice = input(location[3])
            
            if choice.lower() == "west":
                print("You headed back home.\n\n")
                goto(2)

            elif choice.lower() == "south":
                print("You headed towards Oak's Lab.\n\n")
                goto(4)
                
            else:
                messageSorter(choice)

        #Location4: Oak's Lab
        while locCount == 4:
            choice = input(location[4])
            
            if choice.lower() == "north":
                print("You exited the building and started heading towards the tall grass.\n\n")
                goto(3)

            elif choice.lower() == "west":
                print("You walked over to the research room.\n\n")
                goto(5)
                
            else:
                messageSorter(choice)

        #Location5: Reseach Room
        while locCount == 5:
            choice = input(location[5])
            
            if choice.lower() == "east":
                print("You headed back for the lab.\n\n")
                goto(4)

            elif choice.lower() == "south":
                print("You walked toward the battle arena.\n\n")
                goto(6)
                
            else:
                messageSorter(choice)

        #Locaton6: Battle Arena 
        while locCount == 6:
            choice = input(location[6])
            
            if choice.lower() == "north":
                goto(5)

            elif choice.lower() == "west":
                goto(7)

            else:
                messageSorter(choice)

        #Location7: Pokemon Center
        while locCount == 7:
            choice = input(location[7])
            
            if choice.lower() == "east":
                goto(6)

            elif choice.lower() == "north":
                goto(8)

            else:
                messageSorter(choice)

        #Location8: PokeMart
        while locCount == 8:
            choice = input(location[8])
            
            if choice.lower() == "north":
                goto(7)

            elif choice.lower() == "west":
                goto(9)

            else:
                messageSorter(choice)

        #Location9: Rival's House
        if locCount == 9:
            print(location[9])
            getPoints()
            gameFinished = True



        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():

    intro()

    game()
    
    getCopyright()
    
main()
