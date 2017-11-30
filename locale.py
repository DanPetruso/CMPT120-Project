#Dan Petruso
#CMPT 120L 113

from player import *

class Locale:

    def __init__(self, shortLocation, longLocation, items, moveableDirections, itemUsed, usableItem):
        self.shortLocation = shortLocation
        self.longLocation = longLocation
        self.items = items
        self.moveableDirections = moveableDirections
        self.itemUsed = itemUsed
        self.usableItem = usableItem
        visited == False
        
#make a loop that makes all locale objects in project.py
#--------------------------------------------------------------------

    def locationLength(self, count):
        if self.visited == False:
            self.visited == True
            return self.longLocation
        else:
            return self.shortLocation

    def getVisited(self):
        return self.visited

    def itemDrop(self, itemToDrop):
        self.items.append(itemToDrop)

    def itemTake(self, itemToTake):
        itemToTake = itemToTake.lower()
        itemToTake = itemToTake.strip()
        for i in range (0, len(items)):
            if self.items[i] == itemToTake:
                Player.inventory.append(self.items)
                print(itemToTake + " has been added to your inventory.")
            else:
                print("There is no such item here.")

    def searchHere(self):
        print("Items: ", end="")
        for i in range (0, len(self.items)):
            print(self.items[i], end=" ")
        print()

    def canMove(self, direct):
        if moveableDirections != None:
            return True
        return False

    def useItem(self, item):
        if item == self.usableItem:
            print(self.itemUsed)
        else:
            print("You cannot use that item here.")
