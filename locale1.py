#Dan Petruso
#CMPT 120L 113

class Locale:

    def __init__(self, shortLocation, longLocation, items, moveableDirections, itemUsed, usableItem):
        self.shortLocation = shortLocation
        self.longLocation = longLocation
        self.items = items
        self.moveableDirections = moveableDirections
        self.itemUsed = itemUsed
        
        self.usableItem = usableItem
        self.visited = False
        self.wasSearched = False

        #makes sure user uses an item to progress only when there is an item to use
        if usableItem == "" or usableItem == "map":
            self.itemUsedFlag = True
        else:
            self.itemUsedFlag = False
        
#--------------------------------------------------------------------

    def locationLength(self):
        if self.visited == False:
            self.visited = True
            return self.longLocation
        else:
            return self.shortLocation

    def getLongLocation(self):
        return self.longLocation
               
    def getMoveableDirections(self):
        return self.moveableDirections

    def getVisited(self):
        return self.visited

    def itemDrop(self, itemDroppedHere):
        self.items.append(itemDroppedHere)

    def itemTake(self, itemToTake, Player):
        itemToTake = itemToTake.lower()
        itemToTake = itemToTake.strip()
        for i in range (0, len(self.items)):
            if self.items[i] == itemToTake:
                return True                
        return False

    def searchHere(self):
        self.wasSearched = True
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
            self.itemUsedFlag = True
        else:
            print("You cannot use that item here.")
