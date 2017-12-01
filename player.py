#Dan Petruso
#CMPT 120L 113

class Player:
    
    def __init__(self, playerName, rivalName, currentLocale):
        self.playerName = playerName
        self.rivalName = rivalName
        self.currentLocale = currentLocale
        self.numOfMoves = 0
        self.points = 0

        self.inventory = []

#---------------------------------------------------------------------------------

    def getLocale(self):
        return self.currentLocale
    
    def updateLocale(self, update):
        self.currentLocale = update
        
    def getHelp(self):
        print("\nValid commands for the game are North, South, East, West, Look, Search, Take, Map, Pokeball, Package."
              "\nNot all commands will work for all locations."
              "\nType Help to review the commands and Quit to exit game.\n")

    def getWrongWay(self):
        print("\nYou cannot move at that direction in this location.")

    def pointChecker(self):
        if self.currentLocale.getVisited == False:
            self.points += 5
            self.currentLocale.getVisited = True

    def getPoints(self):
        return pointChecker(-1)

    def checkForItem(self, check):
        for i in range (0, len(self.inventory)):
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
            self.currentLocale.searchHere()

        elif choice == "take":
            if self.currentLocale.itemTake(item, self) == True:
                self.inventory.append(item)

        elif choice == "use":
            if self.checkForItem(item) == True:
                self.currentLocale.useItem(item)
            else:
                print("You have no such item.")

        elif choice == "drop":
            if self.checkForItem(item) == True:
                for i in range(0, self.inventory):
                    if item == self.inventory[i]:
                        self.inventory.pop(i)

        elif choice == "use" and item == "map":
            if checkForItem("map") == True:
                getMap()

        elif choice == "look":
            print(self.currentLocale.getLongLocation())

        else:
            print("\nError. Invalid command.\n")

#-------------------------------------------------------------------------------

    def goto(self, num):
        moveableDirections = self.currentLocale.getMoveableDirections()
        if moveableDirections[num] == None:
            print("You cannot move in that direction here.")
        else:
            self.pointChecker()
            self.timer()
            return moveableDirections[num]

    def timer(self):
        self.numOfMoves+=1
        print("Total number of moves:", self.numOfMoves)
        if self.numOfMoves == 25:
            print("You have been out for a long time and your mother wants you home.")
            


    def getMap(self):
        print("\nMap:\n"
              "  Viridian Forest           Bedroom ----- Living Room                    \n"
              "         |                                      |                        \n"
              "         |                                      |                        \n"
              "   Route One                       Outside of House ----- Tall Grass    \n"
              "         |                                                       |      \n"
              "         |                                                       |      \n"
              "   Rivals House ----- PokeMart           Research Room  ----- Oaks Lab  \n"
              "                        |		        |                          \n"
              "                  |  		        |                          \n"
              "                  Pokemon Center ----- Battle Arena                     \n\n")



    def directionToNum(self, direction):
        change = {
            "north" : 0,
            "south" : 1,
            "east"  : 2,
            "west"  : 3}
        return change[direction]
