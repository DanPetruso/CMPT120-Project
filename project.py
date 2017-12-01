#Dan Petruso
#CMPT 120L 113

from locale1 import *
from player import *

def initialize(playerName, rivalName):

    longLocation = [ "\nYou are now in your bedroom. You're bed is unmade and you're too lazy to make it. You see something on your desk."
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
                 "\nYou arrived at the Pokemon Center and Nurse Joy said there is a potion you can take. "
                 "You have to pick up a package for the professor at the PokeMart."
                 "\nTo the north is PokeMart. \nTo the east is the research room. "
                 ,#7
                 "\nYou arrived at the PokeMart and have to pick up the package. Professor Oak wants you "
                 "to give it to him at " + rivalName + "'s house."
                 "\nTo the west is " + rivalName + "'s house. \nTo the south is the Pokemon Center. "
                 ,#8
                 "\nYou arrived at " + rivalName + "'s house and Professor Oak would like the package you were supposed to pick up."
                 "\nYou want to get to Viridian Forest to catch a Pikachu but you must get through Route One without encountering any other Pokemon."
                 "\nTo the north is Route One. \nTo the east PokeMart"
                 ,#9
                 "\nYou just stepped onto Route One and Pokemon are everywhere. You do not want to any Pokemon to encounter you."
                 "\nTo the north is Viridian Forest. To the south is " + rivalName + "'s house."
                 ,#10
                 "\nYou are in Viridian Forest and you see the Pikachu that you want to catch."
                 "\nTo the south is Route One."
                 #11
                 ]

    shortLocation = [ "\nYou are now in your bedroom. East is the door to your living room. "
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
                      "\nYou are at " + rivalName + "'s house. East is PokeMart. North is Route One."
                      ,#9
                      "\nYou are now on Route One. South is " + rivalName + "'s house. North is Viridian Forest."
                      ,#10
                      "\nYou are now in Viridian Forest. South is Route One."
                      #11
                      ]

    mapMatrix = [   #  North       South       East        West
                    [  None,       None,       1,          None     ]    #Bedroom       0
                ,   [  None,       2,          None,       0        ]    #Livingroom    1
                ,   [  1,          None,       3,          None     ]    #Outside       2
                ,   [  None,       4,          None,       2        ]    #Tall Grass    3
                ,   [  3,          None,       None,       5        ]    #Oaks Lab      4
                ,   [  None,       6,          4,          None     ]    #Research Room 5
                ,   [  5,          None,       None,       7        ]    #Battle Arena  6
                ,   [  8,          None,       6,          None     ]    #Pkmn Center   7
                ,   [  None,       7,          None,       9        ]    #PokeMart      8
                ,   [  10,         None,       8,          None     ]    #Rivals House  9
                ,   [  11,         9,          None,       None     ]    #Route One     10
                ,   [  None,       10,         None,       None     ]    #Viridian      11
                ]

    defaultItemLocations = [
                         ["map"       ]          #Bedroom        0
                    ,    [            ]          #LivingRoom     1
                    ,    [            ]          #Outside        2
                    ,    [            ]          #Tall Grass     3
                    ,    [            ]          #Oaks Lab       4
                    ,    ["pokeball"  ]          #Research Room  5
                    ,    [            ]          #Battle Arena   6
                    ,    ["potion"    ]          #Pkmn Center    7
                    ,    ["package", "repel"]    #PokeMart       8
                    ,    ["masterball"]          #Rivals House   9
                    ,    [            ]          #Route One      10
                    ,    [            ]          #Viridian       11
                    ]

    usedItemMessages = [
                            ""#0
                        ,   ""#1
                        ,   ""#2
                        ,   ""#3
                        ,   ""#4
                        ,   ""#5
                        ,   "You threw the pokeball and out came Charmander. You began your "
                              "first battle against " + rivalName + "'s Squirtle."
                              "\nSquirtle used tackle! Charmander used Scratch! Charmander won the battle! "
                              "Charmander is now tired and would like to rest up at the Pokemon Center."#6
                        ,   "You used the potion and healed your Charmander."#7
                        ,   ""#8
                        ,   "You gave Professor Oak the package and now he wants to give you something."#9
                        ,   "You used the repel and now you can continue through Route One."#10
                        ,   "You used the masterball and caught the Pikachu! Congrats, you won!"#11
                        ]

    usableItem = [
                    ""#0
                 ,  ""#1
                 ,  ""#2
                 ,  ""#3
                 ,  ""#4
                 ,  ""#5
                 ,  "pokeball"#6
                 ,  "potion"#7
                 ,  ""#8
                 ,  "package"#9
                 ,  "repel"#10
                 ,  "masterball"#11
                 ]
                    
                            
    localeList = []
    for i in range (0, 12):
        localeList.append( Locale(shortLocation[i], longLocation[i], defaultItemLocations[i],
                                  mapMatrix[i], usedItemMessages[i], usableItem[i]))

    player = Player(playerName, rivalName, localeList[0])

    return localeList, player

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def intro():
    print("Choose Your Pokemon!")
    print("This is a game where you will catch your first Pokemon.")
    print("Every new move you will gain 5 points.")

def customize():
    playerName = input("Professor Oak: 'Welcome to the world of Pokemon, what is your name?' ")

    rivalName = input("Professor Oak: 'Hello " + playerName + ", this is my grandson and your rival, what was his name again?' ")
    
    print("Professor Oak: 'Oh yes, it was " + rivalName + ". Great! Now you have begun your journey!'\n ")

    print("-------------------------------------------------------------------\n")
    return playerName, rivalName

def ending():
    if gameWon == True:
        print("Congrats! You won the game!")
    elif gameWon == False:
        print("Game Over! You didn't complete all the requirements.")
    getCopyright()

def getCopyright():
    print("Copyright (c) 2107 Daniel Petruso, daniel.petruso1@marist.edu")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game(player, localeList):
   
    gameFinished = False
    
    currentLocale = player.getLocale()
    print(player.currentLocale.locationLength())
    move = 0
    
    while player.gameFinished == False:
        
        choice = input()
        choice = choice.lower()
        choice = choice.strip()
        choice = choice.split(" ")
        
        if len(choice) == 1:
            choice.append("")
        
        if choice[0] == "north" or choice[0] == "south" or choice[0] == "east" or choice[0] == "west":
            num = player.directionToNum(choice[0])
            moveNext = player.canMove(num)
            if moveNext != None:
                if player.currentLocale.itemUsedFlag == False and moveNext > move:
                    print("You must use an item first.")
                else:
                    move = moveNext
                    currentLocale = player.updateLocale(localeList[move])
                    player.pointChecker()
                    print("Total points:", player.getPoints())
                    print(player.currentLocale.locationLength())

        else:
            player.messageSorter(choice[0], choice[1])

    if player.gameWon = False:
        print("You lost the game. Better luck next time.")

                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    
    intro()
    playerName, rivalName = customize()
    localeList, player = initialize(playerName, rivalName)
    game(player, localeList)
    ending()
    
main()
