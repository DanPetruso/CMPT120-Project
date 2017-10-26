#Dan Petruso
#CMPT 120L 113
points = 0
visitedLocation = [False, False, False, False, False, False, False, False]
pointGain = 5
gameFinished = False

def intro():
    print("Choose Your Pokemon!")
    print("This is a game where you will choose your first Pokemon and start your first battle.")
    print("Every new move you will gain", pointGain, "points.")

    playerName = input("Professor Oak: 'Welcome to the world of Pokemon, what is your name?' ")

    rivalName = input("Professor Oak: 'Hello " + playerName + ", this is my grandson and your rival, what was his name again?' ")
    
    print("Professor Oak: 'Oh yes, it was " + rivalName + ". Great! Now you have begun your journey!'\n ")

    print("-------------------------------------------------------------------\n")

    return playerName, rivalName

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def getCopyright():
    print("Copyright (c) 2107 Daniel Petruso, daniel.petruso1@marist.edu")

def getHelp():
    print("\nValid commands for the game are North, South, East, West. \nNot all commands will work for all locations."
          "\nType Help to review the commands and Quit to exit game.\n")

def getErrorMessage():
    print("\nError. Invalid command.\n")

def getWrongWay():
    print("\nYou cannot move that direction in this location.")

def messageSorter(choice):
    global gameFinished

    if choice.lower() == "help":
        getHelp()

    elif choice.lower() == "quit":
        gameFinished = True
        print("You just quit the game.")

    elif choice.lower() == "points":
        print("Point total:", getPoints())

    else:
        getErrorMessage()

    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pointChecker(count):
    global points
    global visitedLocation
    global pointGain

    if count == -1: #gives total amount of points to user
        return points
    
    if count == 0 and visitedLocation[0] == False:
        points += pointGain
        visitedLocation[0] = True
        print("Points gained:", pointGain)
        
    if count == 1 and visitedLocation[1] == False:
        points += pointGain
        visitedLocation[1] = True
        print("Points gained:", pointGain)
        
    if count == 2 and visitedLocation[2] == False:
        points += pointGain
        visitedLocation[2] = True
        print("Points gained:", pointGain)
        
    if count == 3 and visitedLocation[3] == False:
        points += pointGain
        visitedLocation[3] = True
        print("Points gained:", pointGain)
        
    if count == 4 and visitedLocation[4] == False:
        points += pointGain
        visitedLocation[4] = True
        print("Points gained:", pointGain)
        
    if count == 5 and visitedLocation[5] == False:
        points += pointGain
        visitedLocation[5] = True
        print("Points gained:", pointGain)

    if count == 6 and visitedLocation[6] == False:
        points += pointGain
        visitedLocation[6] = True
        print("Points gained:", pointGain)

    if count == 7 and visitedLocation[7] == False:
        points += pointGain
        visitedLocation[7] = True
        print("Points gained:", pointGain)


def getPoints():
    return pointChecker(-1)
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game(playerName, rivalName):
    location = [ "You are now in your bedroom. \nTo your east is the door to your living room. ",#0
                 "You are now in your living room. \nTo the south is the front door. \nTo the west is the door to your bedroom. ",#1
                 "You are now outside. \nTo your east is the tall grass. \nTo your north is your house. ",#2
                 "You are now in the tall grass. It is too dangerous to stay here so you will need a Pokemon from Professor Oak to protect yourself."
                 "\nTo the south is Oak's lab. \nTo the west is your house. ",#3
                 "You are now in Oak's lab. He tells you to take the pokeball from the research room to the west.\n"
                 "To the west is the research room. \nTo the north is the exit. ",#4
                 "You are now in the research room and just picked up your pokeball. " + rivalName +  " wants to battle.\n"
                 "To the south is the battle arena. \nTo the east is the lab. ",#5
                 "You entered the battle arena and started your first battle. \n" + playerName + " sent out Charmander. " + rivalName + " sent out Squirtle."
                 "\nSquirtle used tackle. Charmander used scratch. Charmander won the battle!"
                 "\nCharmander is now tired and would like to rest up at the Pokemon Center. \nTo the west is the,"#6
                 ""#7
                 ]
    
    global gameFinished
    locCount = 0

    while gameFinished == False:
        
        #Location0: Bedroom
        while locCount == 0:
            choice = input(location[0])
            
            if choice.lower() == "east":
                print("You proceeded into the living room where your mother is watching television.\n\n")
                pointChecker(locCount)
                locCount = 1
                
            else:
                messageSorter(choice)



                
        #Location1: Living Room
        while locCount == 1:
            choice = input(location[1])
            
            if choice.lower() == "west":
                print("You proceeded back into your room.\n\n")
                locCount = 0

            elif choice.lower() == "south":
                print("You headed out the door. \nMom:'Goodbye", playerName + ", have a nice day!\n\n")
                pointChecker(locCount)
                locCount = 2
                
            else:
                messageSorter(choice)

        #Location2: Outside
        while locCount == 2:
            choice = input(location[2])
            
            if choice.lower() == "north":
                print("You proceeded back into your house.\n\n")
                locCount = 1

            elif choice.lower() == "east":
                print("You headed towards the tall grass.\n\n")
                pointChecker(locCount)
                locCount = 3
                
            else:
                messageSorter(choice)

        #Location3: Tall Grass
        while locCount == 3:
            choice = input(location[3])
            
            if choice.lower() == "west":
                print("You headed back home.\n\n")
                locCount = 2

            elif choice.lower() == "south":
                print("You headed towards Oak's Lab.\n\n")
                pointChecker(locCount)
                locCount = 4
                
            else:
                messageSorter(choice)

        #Location4: Oak's Lab
        while locCount == 4:
            choice = input(location[4])
            
            if choice.lower() == "north":
                print("You exited the building and started heading towards the tall grass.\n\n")
                locCount = 3

            elif choice.lower() == "west":
                print("You walked over to the research room.\n\n")
                pointChecker(locCount)
                locCount = 5
                
            else:
                messageSorter(choice)

        #Location5: Reseach Room
        while locCount == 5:
            choice = input(location[5])
            
            if choice.lower() == "east":
                print("You headed back for the lab.\n\n")
                locCount = 4

            elif choice.lower() == "south":
                print("You walked toward the battle arena.\n\n")
                pointChecker(locCount)
                locCount = 6
                
            else:
                messageSorter(choice)

        #Locaton6: Battle Arena and end of game
        while locCount == 6:
            print(location[6])
            print(playerName, "sent out Charmander.", rivalName, "sent out Squirtle."
                  "\nSquirtle used tackle. Charmander used scratch. Charmander won the battle!")
            gameFinished = True

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main(): 

    playerName, rivalName = intro()

    game(playerName, rivalName)
    
    getCopyright()
    
main()
