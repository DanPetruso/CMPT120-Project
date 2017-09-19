#Dan Petruso
def projOne():

    #program emulates the introduction to the first Pokemon game
    
    name = "Red"
    rivalsName = "Blue"

    points = 0
    pointGain = 10
    
    playersPokemon = "Charmander"
    rivalsPokemon = "Squirtle"

    attack1 = "Scratch"
    attack2 = "Tackle"
    
    print("This is a game where you will choose your first Pokemon.")
    print("Every new move you will gain " + str(pointGain) + " points.")
    print("Professor Oak: 'Welcome to the world of Pokemon, what is your name?'")
    
    input("Press enter to respond.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print("Professor Oak: 'Hello " + name + ", this is my grandson and your rival, what was his name again?'")
    input("Press enter to respond.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print("Professor Oak: 'Oh yes, it was " + rivalsName + ". Great! Now you have begun your journey!'")

    print("-------------------------------------------------------------------")
    input("You are now in your room, press enter to continue.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    input("You have just left your room and exited your home. Press enter to walk towards the tall grass.")
    points += pointGain
    print("You gained " + str(pointGain) + ", your total point count is " + str(points) + ".")

    print("You see Professor Oak run towards you as you approach the grass.")
    print("Professor Oak: 'Wait, " + name + " don't go there! Wild Pokemon live there. You must have a Pokemon to protect yourself. Come to my lab and I will give you one alongside my grandson" + rivalsName + ".")
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

    print("Copywrite (c) 2107 Daniel Petruso, daniel.petruso1@marist.edu")
