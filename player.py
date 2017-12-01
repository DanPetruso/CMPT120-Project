#Dan Petruso
#CMPT 120L 113

class Player:
    
    def __init__(self, playerName, rivalName, currentLocale):
        self.playerName = playerName
        self.rivalName = rivalName
        self.currentLocale = currentLocale
        self.numOfMoves = 0
        self.points = 0
        self.gameFinished = False

        self.inventory = []

#---------------------------------------------------------------------------------

    def getLocale(self):
        return self.currentLocale
    
    def updateLocale(self, update):
        self.currentLocale = update
        
    def getHelp(self):
        print("\nValid commands for the game are North, South, East, West, Look, Search, Take, Use, Search, Quit, Drop, Inventory."
              "\nNot all commands will work for all locations."
              "\nType Help to review the commands and Quit to exit game.\n")

    def getWrongWay(self):
        print("\nYou cannot move at that direction in this location.")

    def pointChecker(self):
        if self.currentLocale.getVisited() == False:
            self.points += 5

    def getPoints(self):
        return self.points

    def checkForItem(self, check):
        for i in range (0, len(self.inventory)):
            if self.inventory[i] == check:
                return True
        return False

    def messageSorter(self, choice, item):
        
        if choice == "help":
            self.getHelp()

        elif choice == "quit":
            gameFinished = True
            print("You just quit the game.")

        elif choice == "points":
            print("Total points:", self.getPoints())

        elif choice == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
            self.getWrongWay()

        elif choice == "search":
            self.currentLocale.searchHere()

        elif choice == "take":
            if self.currentLocale.wasSearched == False:
                print("You must search here first.")
            else:
                if self.currentLocale.itemTake(item, self) == True:
                    self.inventory.append(item)
                    print("You obtained the " + item + "!")
                    index = self.currentLocale.items.index(item)
                    self.currentLocale.items.pop(index)
                else:
                    print("There is no such item here.")

        elif choice == "use" and item == "map":
            if self.checkForItem("map") == True:
                self.getMap()
            else:
                print("You do not have the map.")
                
        elif choice == "use":
            if self.checkForItem(item) == True:
                self.currentLocale.useItem(item)
            else:
                print("You have no such item.")

        elif choice == "drop":
            if self.checkForItem(item) == True:
                for i in range(0, len(self.inventory)):
                    if item == self.inventory[i]:
                        self.inventory.pop(i)
                        self.currentLocale.itemDrop(item)
                        print("You dropped the " + item + ".")
                        break
            else:
                print("You do not have such an item.")

        elif choice == "look":
            print(self.currentLocale.getLongLocation())

        elif choice == "inventory":
            print("Items: ", end="")
            for i in range (0, len(self.inventory)):
                print(self.inventory[i], end=" ")
            print()

        else:
            print("Error. Invalid command.")

#-------------------------------------------------------------------------------

    def canMove(self, num):
        moveableDirections = self.currentLocale.getMoveableDirections()
        if moveableDirections[num] == None:
            print("You cannot move in that direction here.")
            return None
        else:
            self.timer()
            return moveableDirections[num]

    def timer(self):
        self.numOfMoves+=1
        print("Total number of moves:", self.numOfMoves)
        if self.numOfMoves == 25:
            print("You have been out for a long time and your mother wants you home.")
            self.gameFinished = True
            


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
