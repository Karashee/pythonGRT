print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

choice1 = input('You are at a crossroad. Type "left" or "right": ').lower()

if choice1 == "left":
    choice2 = input('You arrive at a lake. Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive safely. There are 3 doors: red, yellow, and blue. Which do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")