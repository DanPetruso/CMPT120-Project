#Dan Petruso
#CMPT 120L 113

from PLayer import *

class Locale:

    def __init__(self, shortLocation, longLocation, items):
        self.shortLocation = shrotLocation
        self.longLocation = longLocation
        self.items = items
        visited == False


    self.location = [ "\nYou are now in your bedroom. You're bed is unmade and you're too lazy to make it. You see something on your desk."
                 "\nTo your east is the door to your living room. "
                 ,#0
                 "\nYou are now in your living room. Your mother is watching television and you're father is nowhere in site."
                 "\nTo the south is the front door. \nTo the west is the door to your bedroom. "
                 ,#1
                 "\nYou are now outside of your house. You notice a few pidgeys on your front lawn."
                 "\nTo your east is the tall grass. \nTo your north is your house. "
                 ,#2
                 "\nYou are now in the tall grass. It is too dangerous to stay here so you will need a Pokemon "
                 "from Professor Oak to protect yourself."
                 "\nTo the south is Oak's lab. \nTo the west is outside your house. "
                 ,#3
                 "\nYou are now in Oak's lab. He tells you to take the pokeball from the research room to the west."
                 "\nTo the west is the research room. \nTo the north is the exit. "
                 ,#4
                 "\nYou are now in the research room and there are pokeballs everywhere."
                 "\nTo the south is the battle arena. \nTo the east is the lab. "
                 ,#5
                 "\nYou entered the battle arena and " + rivalName + " would like to battle."
                 "\nTo the west is the Pokemon Center. \nTo the north is the research room."
                 ,#6
                 "\nYou arrived at the Pokemon Center and Nurse Joy healed your Pokemon. "
                 "You have to pick up a package for the professor at the PokeMart."
                 "\nTo the north is PokeMart. \nTo the east is the research room. "
                 ,#7
                 "\nYou arrived at the PokeMart and have to pick up the package. Professor Oak wants you "
                 "to give it to him at " + rivalName + "'s house."
                 "\nTo the west is " + rivalName + "'s house. \nTo the south is the Pokemon Center. "
                 ,#8
                 "\nYou arrived at " + rivalName + "'s house and Professor Oak would like the package you were supposed to pick up."
                 #9
                 ]

    self.shortLocation = [ "\nYou are now in your bedroom. East is the door to your living room. "
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

    
    def locationLength(count):
        location
        shortLocation
        visitedLocation
        if visitedLocation[count] == False:
            return location[count]
        else:
            return shortLocation[count]

    

    def getLocation():
        global visitedLocation
        global location
        global shortLocation

    def visit():



    
