#Dan Petruso
#CMPT 120L 113

from Locale import *

class Player:
    
    def __init__(self, playerName, rivalName, points):
        self.playerName = playerName
        self.rivalName = rivalName
        self.points = points

        self.inventory = ["map", "pokeball", "package"]
        self.canUse = [False, False, False]


    def getHelp():
        print("\nValid commands for the game are North, South, East, West, Look, Search, Take, Map, Pokeball, Package."
          "\nNot all commands will work for all locations."
          "\nType Help to review the commands and Quit to exit game.\n")

    def getErrorMessage():
        print("\nError. Invalid command.\n")

    def getWrongWay():
        print("\nYou cannot move at that direction in this location.")

    def getLongLocation():
        global location
        global locCount
        print(location[locCount])

    def getSearch():
        global locCount
        global searchLocation
        print(searchLocation[locCount])

    def takeItem():
        global locCount
        global canUse
        if locCount == 0:
            canUse[0] = True
            print("You took the map.")
        if locCount == 5:
            canUse[1] = True
            print("You took the pokeball.")
        if locCount == 8:
            canUse[2] = True
            print("You took the package.")

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

    def getPoints():
        return pointChecker(-1)

    def goto(counter):
        if counter == None:
            print("You cannot move in that direction here.")
        else:
            pointChecker(locCount)
            locCount = counter
            print(locationLength(locCount))
            timer()

    def timer():
        global numOfMoves
        global locCount
        global gameFinished
        numOfMoves+=1
        print("Total number of moves:", numOfMoves)
        if numOfMoves == 18:
            print("You have been out for a long time and your mother wants you home.")
            gameFinished = True


    def messageSorter(choice):
        global gameFinished
        global inventory
        global canUse
        global gameWon

        if choice == "help":
            getHelp()

        elif choice == "quit":
            gameFinished = True
            print("You just quit the game.")

        elif choice == "points":
            getPoints()

        elif choice == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
            getWrongWay()

        elif choice == inventory[0]:#map
            if canUse[0] == True:
                getMap()
            else:
                print("You do not have the map yet.")

        elif choice == inventory[1]:#pokeball
            if canUse[1] == True and locCount == 6:
                print("You threw the pokeball and out came Charmander. You began your "
                      "first battle against " + rivalName + "'s Squirtle."
                      "\nSquirtle used tackle! Charmander used Scratch! Charmander won the battle! "
                      "Charmander is now tired and would like to rest up at the Pokemon Center.")
            elif canUse[1] == False:
                print("You do not have the pokeball yet.")
            else:
                print("You cannot use that in this location.")

        elif choice == inventory[2]:#package
            if canUse[2] == True and locCount == 9:
                print("You delivered the package to Professor Oak. In return, he rewards you with a Pokedex.")
                gameFinished = True
                gameWon = True
            elif canUse[2] == False:
                print("You do not have the package yet.")
            else:
                print("You cannot use that here.")

        elif choice == "search":
            getSearch()

        elif choice == "take":
            takeItem()

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
