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

    def getHelp(self):
        print("\nValid commands for the game are North, South, East, West, Look, Search, Take, Map, Pokeball, Package."
          "\nNot all commands will work for all locations."
          "\nType Help to review the commands and Quit to exit game.\n")

    def getErrorMessage(self):
        print("\nError. Invalid command.\n")

    def getWrongWay(self):
        print("\nYou cannot move at that direction in this location.")

    def getSearch(self):
        print(searchLocation[locCount])

    def pointChecker(self, count):
        global points
        global visitedLocation
        global pointGain
        global locCount

        if count == -1: #gives total amount of points to user
            print("\nTotal points: " + str(points))

        if visitedLocation[locCount] == False:
            points += pointGain
            visitedLocation[locCount] = True

    def getPoints(self):
        return pointChecker(-1)

        def messageSorter(choice, item):
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


        #make a for loop that goes thru the inventory array to check for items
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

        ##############-----------

        elif choice == "search":
            getSearch()

        elif choice == "take":
            Locale.itemTake(item)

        elif choice == "look":
            Locale.getLongLocation()

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
