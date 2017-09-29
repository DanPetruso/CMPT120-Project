#Dan Petruso
points = 0
loc0, loc1, loc2, loc3, loc4, loc5 = False, False, False, False, False, False
pointGain = 5

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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pointChecker(count):
    global points
    global loc0, loc1, loc2, loc3, loc4, loc5
    global pointGain

    if count == -1: #gives total amount of points to user
        return points
    
    if count == 0 and loc0 == False:
        points += pointGain
        loc0 = True
        print("Points gained:", pointGain, "\nPoint total:", points)
        
    if count == 1 and loc1 == False:
        points += pointGain
        loc1 = True
        print("Points gained:", pointGain, "\nPoint total:", points)
        
    if count == 2 and loc2 == False:
        points += pointGain
        loc2 = True
        print("Points gained:", pointGain, "\nPoint total:", points)
        
    if count == 3 and loc3 == False:
        points += pointGain
        loc3 = True
        print("Points gained:", pointGain, "\nPoint total:", points)
        
    if count == 4 and loc4 == False:
        points += pointGain
        loc4 = True
        print("Points gained:", pointGain, "\nPoint total:", points)
        
    if count == 5 and loc5 == False:
        points += pointGain
        loc5 = True
        print("Points gained:", pointGain, "\nPoint total:", points)


def getPoints():
    return pointChecker(-1)
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game(playerName, rivalName):
    location = [ "You are now in your bedroom. \nTo your east is the door to your living room.",#0
                 "You are now in your living room. \nTo the south is the front door. \nTo the west is the door to your bedroom.",#1
                 "You are now outside. \nTo your east is the tall grass. \nTo your north is your house.",#2
                 "You are now in the tall grass. It is too dangerous to stay here so you will need a Pokemon from Professor Oak to protect yourself."
                 "\nTo the south is Oak's lab. \nTo the west is your house.",#3
                 "You are now in Oak's lab. He tells you to take the pokeball from the research room to the west.\n"
                 "To the west is the research room. \nTo the north is the exit.",#4
                 "You are now in the research room and just picked up your pokeball. " + rivalName +  " wants to battle.\n"
                 "To the south is the battle arena. \nTo the east is the lab.",#5
                 "You entered the battle arena and started your first battle."] #6
    
    gameFinished = False
    locCount = 0

    while gameFinished == False:
        
        #Location0: Bedroom
        if locCount == 0:
            
            while locCount == 0:
                choice = input(location[0])
                
                if choice.lower() == "east":
                    print("You proceeded into the living room where your mother is watching television.\n\n")
                    pointChecker(locCount)
                    locCount+=1
                    
                elif choice.lower() == "help":
                    getHelp()

                elif choice.lower() == "quit":
                    gameFinished = True
                    print("You just quit the game.")
                    break

                else:
                    getErrorMessage()

        #Location1: Living Room
        if locCount == 1:

            while locCount == 1:
                choice = input(location[1])
                
                if choice.lower() == "west":
                    print("You proceeded back into your room.\n\n")
                    locCount-=1

                elif choice.lower() == "south":
                    print("You headed out the door. \nMom:'Goodbye", playerName + ", have a nice day!\n\n")
                    pointChecker(locCount)
                    locCount+=1
                    
                elif choice.lower() == "help":
                    getHelp()

                elif choice.lower() == "quit":
                    gameFinished = True
                    print("You just quit the game.")
                    break

                else:
                    getErrorMessage()


        #Location2: Outside
        if locCount == 2:

            while locCount == 2:
                choice = input(location[2])
                
                if choice.lower() == "north":
                    print("You proceeded back into your house.\n\n")
                    locCount-=1

                elif choice.lower() == "east":
                    print("You headed towards the tall grass. \n\n")
                    pointChecker(locCount)
                    locCount+=1
                    
                elif choice.lower() == "help":
                    getHelp()

                elif choice.lower() == "quit":
                    gameFinished = True
                    print("You just quit the game.")
                    break

                else:
                    getErrorMessage()


        #Location3: Tall Grass
        if locCount == 3:

            while locCount == 3:
                choice = input(location[3])
                
                if choice.lower() == "west":
                    print("You headed back home.\n\n")
                    locCount-=1

                elif choice.lower() == "south":
                    print("You headed towards Oak's Lab.\n\n")
                    pointChecker(locCount)
                    locCount+=1
                    
                elif choice.lower() == "help":
                    getHelp()

                elif choice.lower() == "quit":
                    gameFinished = True
                    print("You just quit the game.")
                    break

                else:
                    getErrorMessage()


        #Location4: Oak's Lab
        if locCount == 4:

            while locCount == 4:
                choice = input(location[4])
                
                if choice.lower() == "north":
                    print("You exited the building and started heading towards the tall grass.\n\n")
                    locCount-=1

                elif choice.lower() == "west":
                    print("You walked over to the research room.\n\n")
                    pointChecker(locCount)
                    locCount+=1
                    
                elif choice.lower() == "help":
                    getHelp()

                elif choice.lower() == "quit":
                    gameFinished = True
                    print("You just quit the game.")
                    break

                else:
                    getErrorMessage()


        #Location5: Reseach Room
        if locCount == 5:

            while locCount == 5:
                choice = input(location[5])
                
                if choice.lower() == "east":
                    print("You headed back for the lab.\n\n")
                    locCount-=1

                elif choice.lower() == "south":
                    print("You walked toward the battle arena.\n\n")
                    pointChecker(locCount)
                    locCount+=1
                    
                elif choice.lower() == "help":
                    getHelp()

                elif choice.lower() == "quit":
                    gameFinished = True
                    print("You just quit the game.")
                    break

                else:
                    getErrorMessage()


        #Locaton6: Battle Arena and end of game
        if locCount == 6:
            print(location[6])
            print("Congratulations " + playerName + " you won the game with " + str(getPoints()) + " points!")
            gameFinished = True

        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main(): 

    playerName, rivalName = intro()

    game(playerName, rivalName)
    
    getCopyright()
    
main()
