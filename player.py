#Dan Petruso
#CMPT 120L 113

from locale import *

class Player:
    
    def __init__(self, playerName, rivalName, points):
        self.playerName = playerName
        self.rivalName = rivalName
        self.points = points

        self.inventory = []


#change everything like locCount and make it just current Locale object
#---------------------------------------------------------------------------------

    def getLocale(self):
        return currentLocale

    def startingLocale(self, start):
        self.currentLocale = start
        
    def updateLocale(self, update):
        self.currentLocale = update
        
    def getHelp(self):
        print("\nValid commands for the game are North, South, East, West, Look, Search, Take, Map, Pokeball, Package."
              "\nNot all commands will work for all locations."
              "\nType Help to review the commands and Quit to exit game.\n")

    def getErrorMessage(self):
        print("\nError. Invalid command.\n")

    def getWrongWay(self):
        print("\nYou cannot move at that direction in this location.")

    def pointChecker(self, count):
        if count == -1: #gives total amount of points to user
            print("\nTotal points: " + str(self.points))

        if currentLocale.getVisited == False:
            self.points += 5
            currentLocale.getVisited = True

    def getPoints(self):
        return pointChecker(-1)

    def checkForItem(self, check):
        for i in range (0, self.inventory):
            if self.inventory[i] == check:
                return True
        return False

    def messageSorter(self, choice, item):
        
        if choice == "help":
            getHelp()

        elif choice == "quit":
            gameFinished = True
            print("You just quit the game.")

        elif choice == "points":
            getPoints()

        elif choice == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
            getWrongWay()

        elif choice == "search":
            currentLocale.searchHere()

        elif choice == "take":
            currentLocale.itemTake(item)

        elif choice == "use":
            if checkForItem(item) == True:
                currentLocale.useItem(item)
            else:
                print("You have no such item.")

        elif choice == "use" and item == "map":
            if checkForItem("map") == True:
                getMap()

        elif choice == "look":
            currentLocale.getLongLocation()

        else:
            getErrorMessage()

#-------------------------------------------------------------------------------

    def goto(counter):
        if counter == None:
            print("You cannot move in that direction here.")
        else:
            pointChecker(locCount)
            locCount = counter
            print(locationLength(locCount))
            timer()

    def timer():
        numOfMoves+=1
        print("Total number of moves:", numOfMoves)
        if numOfMoves == 18:
            print("You have been out for a long time and your mother wants you home.")
            gameFinished = True


    def getMap():
        print("\nMap:\n"
              "  Viridian Forest           Bedroom ----- Living Room                    \n"
              "         |                                      |                        \n"
              "         |                                      |                        \n"
              "   Route One                       Outside of House ----- Tall Grass    \n"
              "         |                                                       |      \n"
              "         |                                                       |      \n"
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
