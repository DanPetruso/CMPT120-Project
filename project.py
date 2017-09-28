#Dan Petruso

pointGain = 10
points = 0
loc0, loc1, loc2, loc3, loc4, loc5 = False

def intro():
    print("This is a game where you will choose your first Pokemon and engage in your first battle.")
    print("Every new move you will gain " + str(pointGain) + " points.")

    playerName = input("Professor Oak: 'Welcome to the world of Pokemon, what is your name?")

    rivalName = input("Professor Oak: 'Hello " + name + ", this is my grandson and your rival, what was his name again?")
    
    print("Professor Oak: 'Oh yes, it was " + rivalsName + ". Great! Now you have begun your journey!/n")

    print("-------------------------------------------------------------------/n")

    return playerName, rivalName

def getCopyright():
    print("Copywrite (c) 2107 Daniel Petruso, daniel.petruso1@marist.edu")

def getHelp():
    ("Valid commands for the game are North, South, East, West, Help, and Quit.")

def pointChecker():
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game():
    location = [ "You are now in your bedroom. /nTo your north is the stairs.",#0
                 "You are now in your living room. /nTo the south is the front door. /nTo the north is the stairs to your bedrrom.",#1
                 "You are now outside. /nTo your east is the tall grass. /nTo your north is your house.",#2
                 "You are now in the tall grass but Professor Oak stops you and says you cannot continue walking that way without a Pokemon. He invites you to his lab."
                 "/nTo the south is Oaks lab. /nTo the west is your house.",#3
                 "You are now in Oaks lab. He tells you to take the pokeball on the desk. /nTo the east is the desk. /nTo the north is the exit.",#4
                 "You are at the desk and just picked up your pokeball.", rivalName, "wants to battle. /nTo the south is the battle arena. /nTo the north is the exit."]#5
    
    gameFinished = False
    locCount = 0

    while gameFinished == False:
        
        #Location0: Bedroom
        if locCount == 0:
            while locCount == 0:
                choice = input(location[0])
                if choice.lower() == "north":
                    print("You proceeded down the stairs./n/n")
                    locCount = 1
                    
                elif
        
    
 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():    
    

    
    playersPokemon = "Charmander"
    rivalsPokemon = "Squirtle"

    attack1 = "Scratch"
    attack2 = "Tackle"

    playerName, rivalName = intro()
    
    input("You are now in your room, press enter to continue.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    input("You have just left your room and exited your home. Press enter to walk towards the tall grass.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print("You see Professor Oak run towards you as you approach the grass.")
    print("Professor Oak: 'Wait, " + name + " don't go there! Wild Pokemon live there. You must have a Pokemon to protect yourself."
          "Come to my lab and I will give you one alongside my grandson" + rivalsName + ".")
                 
    input("Press enter to walk into Oak's lab.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print("Professor Oak: 'There are three Pokemon here, Bulbasaur, Charmander, and Squirtle. " + name + ",please choose one first.")
    print(rivalsName + ": 'But gramps, why does he get to choose first!")
    print("Professor Oak: 'Calm down " + rivalsName + " you get to choose next.")

    input("Now it's time to choose Blubasaur, Charmander, or Squirtle, press enter to choose.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print(name + " chose " + playersPokemon + "!")
    print(rivalsName + ": In that case, I'll choose " + rivalsPokemon + ".")

    input("Press enter to leave the lab.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print(rivalsName + ": Wait up, we just got our Pokemon, let's battle!")
    input("Press enter to send out " + playersPokemon + " to start the battle.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print("-------------------------------------------------------------------")
    print("Your " + playersPokemon + " is now battling " + rivalsName + "'s " + rivalsPokemon + ".")

    input("Press enter to attack.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print(playersPokemon + " used ", attack1 + "!")
    print(rivalsPokemon + " used ", attack2 + "!")

    input("Press enter to attack again.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print(playersPokemon + " used ", attack1 + "!")
    print(rivalsPokemon + " fainted!")

    print("Congratulations, you won the battle!")
    print("Your total point count is " + str(points) + ".")
    
    getCopyright()
    
main()
